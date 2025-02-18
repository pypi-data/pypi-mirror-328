\echo 'Table Statistics:'
SELECT 
    schemaname as schema,
    relname as table,
    n_live_tup as row_count
FROM pg_stat_user_tables
WHERE schemaname = 'ttt'
ORDER BY relname;

\echo '\nSample Persons:'
SELECT * FROM ttt.ttz_person LIMIT 3;

\echo '\nSample Qualifications:'
SELECT * FROM ttt.ttz_qualification LIMIT 3;

\echo '\nSample Person Qualifications:'
SELECT * FROM ttt.ttz_person_qualification LIMIT 3;
