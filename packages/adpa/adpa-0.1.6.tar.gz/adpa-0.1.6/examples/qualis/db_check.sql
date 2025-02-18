-- Check if schema exists
SELECT schema_name, schema_owner 
FROM information_schema.schemata 
WHERE schema_name = 'ttt';

-- List all tables in the ttt schema
SELECT table_name, table_type
FROM information_schema.tables 
WHERE table_schema = 'ttt'
ORDER BY table_name;

-- Get column information for all tables in ttt schema
SELECT 
    t.table_name,
    c.column_name,
    c.data_type,
    c.character_maximum_length,
    c.is_nullable,
    c.column_default
FROM information_schema.tables t
JOIN information_schema.columns c 
    ON t.table_name = c.table_name 
    AND t.table_schema = c.table_schema
WHERE t.table_schema = 'ttt'
ORDER BY t.table_name, c.ordinal_position;

-- Get row counts for each table
SELECT 
    schemaname as schema,
    relname as table,
    n_live_tup as row_count
FROM pg_stat_user_tables
WHERE schemaname = 'ttt'
ORDER BY relname;
