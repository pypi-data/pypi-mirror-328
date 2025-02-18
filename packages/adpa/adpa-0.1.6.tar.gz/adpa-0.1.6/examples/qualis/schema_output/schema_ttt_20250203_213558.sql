-- Schema: ttt
-- Extracted: 2025-02-03T21:35:58.398692

CREATE SCHEMA IF NOT EXISTS ttt;

-- Sequences
CREATE SEQUENCE IF NOT EXISTS ttt.ttz_person_person_id_seq;
CREATE SEQUENCE IF NOT EXISTS ttt.ttz_person_qualification_person_qualification_id_seq;
CREATE SEQUENCE IF NOT EXISTS ttt.ttz_qualification_qualification_id_seq;

-- Table: ttz_person
CREATE TABLE ttt.ttz_person (
    id integer NOT NULL DEFAULT nextval('ttt.ttz_person_person_id_seq'::regclass),
    first_name character varying(100),
    last_name character varying(100),
    email character varying(255),
    birth_date date,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    person_id integer,
    PRIMARY KEY (id)
);

-- Add indexes for ttz_person
CREATE INDEX idx_person_email ON ttt.ttz_person(email);
CREATE INDEX idx_person_names ON ttt.ttz_person(last_name, first_name);
CREATE INDEX idx_person_birth_date ON ttt.ttz_person(birth_date);

-- Table: ttz_qualification
CREATE TABLE ttt.ttz_qualification (
    qualification_id integer NOT NULL DEFAULT nextval('ttt.ttz_qualification_qualification_id_seq'::regclass),
    name character varying(255) NOT NULL,
    description text,
    level integer,
    valid_from date,
    valid_until date,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    language_id character varying(12),
    PRIMARY KEY (qualification_id)
);

-- Add indexes for ttz_qualification
CREATE INDEX idx_qualification_name ON ttt.ttz_qualification(name);
CREATE INDEX idx_qualification_validity ON ttt.ttz_qualification(valid_from, valid_until);
CREATE INDEX idx_qualification_language ON ttt.ttz_qualification(language_id);

-- Table: ttz_person_qualification
CREATE TABLE ttt.ttz_person_qualification (
    person_qualification_id integer NOT NULL DEFAULT nextval('ttt.ttz_person_qualification_person_qualification_id_seq'::regclass),
    person_id integer,
    qualification_id integer,
    acquired_date date,
    expiry_date date,
    status character varying(50),
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    valid_from integer,
    valid_until integer,
    competency_id integer,
    info_rec_id integer,
    changed_at integer,
    changed_from character varying(255),
    PRIMARY KEY (person_qualification_id),
    FOREIGN KEY (person_id) REFERENCES ttt.ttz_person(id) ON DELETE CASCADE,
    FOREIGN KEY (qualification_id) REFERENCES ttt.ttz_qualification(qualification_id) ON DELETE CASCADE
);

-- Add indexes for ttz_person_qualification
CREATE INDEX idx_person_qual_person ON ttt.ttz_person_qualification(person_id);
CREATE INDEX idx_person_qual_qualification ON ttt.ttz_person_qualification(qualification_id);
CREATE INDEX idx_person_qual_dates ON ttt.ttz_person_qualification(acquired_date, expiry_date);
CREATE INDEX idx_person_qual_validity ON ttt.ttz_person_qualification(valid_from, valid_until);
CREATE INDEX idx_person_qual_status ON ttt.ttz_person_qualification(status);

-- Add triggers for updated_at timestamps
CREATE OR REPLACE FUNCTION ttt.update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_person_updated_at
    BEFORE UPDATE ON ttt.ttz_person
    FOR EACH ROW
    EXECUTE FUNCTION ttt.update_updated_at_column();

CREATE TRIGGER update_qualification_updated_at
    BEFORE UPDATE ON ttt.ttz_qualification
    FOR EACH ROW
    EXECUTE FUNCTION ttt.update_updated_at_column();

CREATE TRIGGER update_person_qualification_updated_at
    BEFORE UPDATE ON ttt.ttz_person_qualification
    FOR EACH ROW
    EXECUTE FUNCTION ttt.update_updated_at_column();

-- Add comments
COMMENT ON TABLE ttt.ttz_person IS 'Stores information about persons';
COMMENT ON TABLE ttt.ttz_qualification IS 'Stores available qualifications';
COMMENT ON TABLE ttt.ttz_person_qualification IS 'Links persons to their qualifications with validity periods';

-- Add table constraints
ALTER TABLE ttt.ttz_person 
    ADD CONSTRAINT chk_person_email_format 
    CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

ALTER TABLE ttt.ttz_qualification 
    ADD CONSTRAINT chk_qualification_dates 
    CHECK (valid_from <= valid_until);

ALTER TABLE ttt.ttz_person_qualification 
    ADD CONSTRAINT chk_person_qual_dates 
    CHECK (acquired_date <= expiry_date);

-- Create views for common queries
CREATE OR REPLACE VIEW ttt.vw_active_qualifications AS
SELECT 
    p.id as person_id,
    p.first_name,
    p.last_name,
    q.qualification_id,
    q.name as qualification_name,
    pq.acquired_date,
    pq.expiry_date,
    pq.status
FROM ttt.ttz_person p
JOIN ttt.ttz_person_qualification pq ON p.id = pq.person_id
JOIN ttt.ttz_qualification q ON pq.qualification_id = q.qualification_id
WHERE (pq.expiry_date IS NULL OR pq.expiry_date >= CURRENT_DATE)
AND (q.valid_until IS NULL OR q.valid_until >= CURRENT_DATE);

COMMENT ON VIEW ttt.vw_active_qualifications IS 'Shows all active qualifications for persons';
