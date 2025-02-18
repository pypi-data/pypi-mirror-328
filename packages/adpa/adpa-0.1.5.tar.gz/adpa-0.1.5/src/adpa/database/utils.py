"""
Database utility functions.
"""
from typing import List, Dict, Any, Optional, Set
import logging
from sqlalchemy import inspect, text
from sqlalchemy.engine import Engine
from sqlalchemy.schema import Table
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

class DatabaseUtils:
    """Database utility functions."""
    
    @staticmethod
    def get_table_names(engine: Engine) -> List[str]:
        """Get all table names in database.
        
        Args:
            engine: Database engine
            
        Returns:
            List of table names
        """
        inspector = inspect(engine)
        return inspector.get_table_names()
    
    @staticmethod
    def get_table_columns(
        engine: Engine,
        table_name: str
    ) -> List[Dict[str, Any]]:
        """Get column information for a table.
        
        Args:
            engine: Database engine
            table_name: Name of table
            
        Returns:
            List of column information
        """
        inspector = inspect(engine)
        return inspector.get_columns(table_name)
    
    @staticmethod
    def get_primary_keys(
        engine: Engine,
        table_name: str
    ) -> List[str]:
        """Get primary key columns for a table.
        
        Args:
            engine: Database engine
            table_name: Name of table
            
        Returns:
            List of primary key column names
        """
        inspector = inspect(engine)
        return [
            pk["name"]
            for pk in inspector.get_pk_constraint(table_name)["constrained_columns"]
        ]
    
    @staticmethod
    def get_foreign_keys(
        engine: Engine,
        table_name: str
    ) -> List[Dict[str, Any]]:
        """Get foreign key information for a table.
        
        Args:
            engine: Database engine
            table_name: Name of table
            
        Returns:
            List of foreign key information
        """
        inspector = inspect(engine)
        return inspector.get_foreign_keys(table_name)
    
    @staticmethod
    def get_indexes(
        engine: Engine,
        table_name: str
    ) -> List[Dict[str, Any]]:
        """Get index information for a table.
        
        Args:
            engine: Database engine
            table_name: Name of table
            
        Returns:
            List of index information
        """
        inspector = inspect(engine)
        return inspector.get_indexes(table_name)
    
    @staticmethod
    def get_table_schema(
        engine: Engine,
        table_name: str
    ) -> Dict[str, Any]:
        """Get complete schema information for a table.
        
        Args:
            engine: Database engine
            table_name: Name of table
            
        Returns:
            Dictionary with table schema information
        """
        return {
            "columns": DatabaseUtils.get_table_columns(engine, table_name),
            "primary_keys": DatabaseUtils.get_primary_keys(engine, table_name),
            "foreign_keys": DatabaseUtils.get_foreign_keys(engine, table_name),
            "indexes": DatabaseUtils.get_indexes(engine, table_name)
        }
    
    @staticmethod
    def get_table_dependencies(
        engine: Engine,
        table_name: str
    ) -> Dict[str, Set[str]]:
        """Get dependencies for a table.
        
        Args:
            engine: Database engine
            table_name: Name of table
            
        Returns:
            Dictionary with incoming and outgoing dependencies
        """
        inspector = inspect(engine)
        incoming = set()
        outgoing = set()
        
        # Check incoming foreign keys
        for table in inspector.get_table_names():
            for fk in inspector.get_foreign_keys(table):
                if fk["referred_table"] == table_name:
                    incoming.add(table)
        
        # Check outgoing foreign keys
        for fk in inspector.get_foreign_keys(table_name):
            outgoing.add(fk["referred_table"])
        
        return {
            "incoming": incoming,
            "outgoing": outgoing
        }
    
    @staticmethod
    def analyze_table(
        session: Session,
        table_name: str
    ) -> Dict[str, Any]:
        """Analyze table statistics.
        
        Args:
            session: Database session
            table_name: Name of table
            
        Returns:
            Dictionary with table statistics
        """
        stats = {}
        
        # Get row count
        count = session.execute(
            text(f"SELECT COUNT(*) FROM {table_name}")
        ).scalar()
        stats["row_count"] = count
        
        # Get size information
        size_query = text(f"""
            SELECT
                pg_size_pretty(pg_total_relation_size('{table_name}')),
                pg_size_pretty(pg_relation_size('{table_name}')),
                pg_size_pretty(pg_total_relation_size('{table_name}') -
                             pg_relation_size('{table_name}'))
        """)
        total_size, table_size, index_size = session.execute(size_query).first()
        
        stats["size"] = {
            "total": total_size,
            "table": table_size,
            "index": index_size
        }
        
        # Get basic column statistics
        stats["columns"] = {}
        for column in DatabaseUtils.get_table_columns(session.get_bind(), table_name):
            col_name = column["name"]
            col_stats = session.execute(text(f"""
                SELECT
                    COUNT(DISTINCT {col_name}),
                    COUNT({col_name}),
                    pg_size_pretty(SUM(pg_column_size({col_name})))
                FROM {table_name}
            """)).first()
            
            stats["columns"][col_name] = {
                "distinct_values": col_stats[0],
                "non_null_values": col_stats[1],
                "total_size": col_stats[2]
            }
        
        return stats
    
    @staticmethod
    def check_table_health(
        session: Session,
        table_name: str
    ) -> Dict[str, Any]:
        """Check table health.
        
        Args:
            session: Database session
            table_name: Name of table
            
        Returns:
            Dictionary with health information
        """
        health = {}
        
        # Check for bloat
        bloat_query = text(f"""
            SELECT
                current_database(),
                schemaname,
                tablename,
                ROUND(CASE WHEN otta=0 THEN 0.0
                    ELSE sml.relpages/otta::numeric END,1) AS bloat_ratio,
                CASE WHEN relpages < otta THEN '0'
                    ELSE pg_size_pretty((bs*(sml.relpages-otta)::bigint)::bigint)
                END AS bloat_size
            FROM (
                SELECT
                    schemaname, tablename, cc.reltuples, cc.relpages, bs,
                    CEIL((cc.reltuples*((datahdr+ma-
                        (CASE WHEN datahdr%ma=0 THEN ma ELSE datahdr%ma END))+nullhdr2+4))/(bs-20::float)) AS otta
                FROM (
                    SELECT
                        ma,bs,schemaname,tablename,
                        (datawidth+(hdr+ma-(case when hdr%ma=0 THEN ma ELSE hdr%ma END)))::numeric AS datahdr,
                        (maxfracsum*(nullhdr+ma-(case when nullhdr%ma=0 THEN ma ELSE nullhdr%ma END))) AS nullhdr2
                    FROM (
                        SELECT
                            schemaname, tablename, hdr, ma, bs,
                            SUM((1-null_frac)*avg_width) AS datawidth,
                            MAX(null_frac) AS maxfracsum,
                            hdr+(
                                SELECT 1+count(*)/8
                                FROM pg_stats s2
                                WHERE null_frac<>0 AND s2.schemaname = s.schemaname AND s2.tablename = s.tablename
                            ) AS nullhdr
                        FROM pg_stats s, (
                            SELECT
                                (SELECT current_setting('block_size')::numeric) AS bs,
                                CASE WHEN substring(v,12,3) IN ('8.0','8.1','8.2') THEN 27 ELSE 23 END AS hdr,
                                CASE WHEN v ~ 'mingw32' THEN 8 ELSE 4 END AS ma
                            FROM (SELECT version() AS v) AS foo
                        ) AS constants
                        GROUP BY 1,2,3,4,5
                    ) AS foo
                ) AS rs
                JOIN pg_class cc ON cc.relname = rs.tablename
                JOIN pg_namespace nn ON cc.relnamespace = nn.oid AND nn.nspname = rs.schemaname
            ) AS sml
            WHERE schemaname = 'public'
            AND tablename = :table_name
        """)
        
        try:
            bloat = session.execute(
                bloat_query,
                {"table_name": table_name}
            ).first()
            if bloat:
                health["bloat"] = {
                    "ratio": float(bloat[3]),
                    "size": bloat[4]
                }
        except Exception as e:
            logger.warning(f"Failed to check bloat for {table_name}: {e}")
        
        # Check for dead tuples
        try:
            dead_tuples = session.execute(text(f"""
                SELECT
                    n_dead_tup,
                    n_live_tup,
                    CASE
                        WHEN n_live_tup = 0 THEN 0
                        ELSE n_dead_tup::float / n_live_tup
                    END AS dead_ratio
                FROM pg_stat_user_tables
                WHERE relname = :table_name
            """), {"table_name": table_name}).first()
            
            if dead_tuples:
                health["dead_tuples"] = {
                    "count": dead_tuples[0],
                    "ratio": float(dead_tuples[2])
                }
        except Exception as e:
            logger.warning(f"Failed to check dead tuples for {table_name}: {e}")
        
        return health
