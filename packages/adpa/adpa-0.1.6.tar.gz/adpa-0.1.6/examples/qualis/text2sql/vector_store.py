"""Vector store component for storing and retrieving schema and training data."""
from typing import Dict, List, Optional, Tuple, Set
import json
from datetime import datetime, timedelta
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import pandas as pd

class VectorStore:
    def __init__(self, persist_directory: str):
        """Initialize vector store with persistence."""
        self.client = chromadb.Client(Settings(
            persist_directory=persist_directory,
            anonymized_telemetry=False
        ))
        
        # Use all-MiniLM-L6-v2 for better semantic search
        self.embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        # Create collections for different types of data
        self.schema_collection = self.client.get_or_create_collection(
            name="schema_info",
            embedding_function=self.embedding_func
        )
        
        self.training_collection = self.client.get_or_create_collection(
            name="training_data",
            embedding_function=self.embedding_func
        )
        
        self.query_collection = self.client.get_or_create_collection(
            name="query_history",
            embedding_function=self.embedding_func
        )
        
        # New collection for SQL patterns
        self.pattern_collection = self.client.get_or_create_collection(
            name="sql_patterns",
            embedding_function=self.embedding_func
        )

    def store_schema_info(self, table_name: str, schema_info: Dict) -> None:
        """Store schema information in vector store with enhanced metadata."""
        description = self._create_schema_description(table_name, schema_info)
        column_types = self._extract_column_types(schema_info)
        relationships = self._extract_relationships(schema_info)
        
        self.schema_collection.add(
            documents=[description],
            metadatas=[{
                "table_name": table_name,
                "schema_info": json.dumps(schema_info),
                "column_types": json.dumps(column_types),
                "relationships": json.dumps(relationships),
                "type": "table_schema",
                "timestamp": datetime.now().isoformat(),
                "complexity_score": self._calculate_schema_complexity(schema_info)
            }],
            ids=[f"schema_{table_name}"]
        )

    def _calculate_schema_complexity(self, schema_info: Dict) -> float:
        """Calculate schema complexity score based on various factors."""
        score = 0.0
        # Number of columns
        score += len(schema_info.get("columns", {})) * 0.1
        # Number of relationships
        score += len(schema_info.get("relationships", [])) * 0.2
        # Number of constraints
        constraints = sum(len(col.get("constraints", [])) 
                        for col in schema_info.get("columns", {}).values())
        score += constraints * 0.15
        return score

    def store_training_example(self, question: str, sql: str, 
                             metadata: Optional[Dict] = None,
                             feedback_score: Optional[float] = None) -> None:
        """Store a training example with enhanced metadata."""
        if metadata is None:
            metadata = {}
            
        # Extract SQL patterns
        patterns = self._extract_sql_patterns(sql)
        
        example_id = f"training_{len(self.training_collection.get()['ids'])}"
        
        self.training_collection.add(
            documents=[f"Question: {question}\nSQL: {sql}"],
            metadatas=[{
                "question": question,
                "sql": sql,
                "patterns": json.dumps(patterns),
                "complexity": self._calculate_sql_complexity(sql),
                "feedback_score": feedback_score,
                "timestamp": datetime.now().isoformat(),
                **metadata
            }],
            ids=[example_id]
        )
        
        # Store patterns separately
        for pattern in patterns:
            pattern_id = f"pattern_{hash(pattern)}"
            try:
                self.pattern_collection.add(
                    documents=[pattern],
                    metadatas=[{
                        "pattern": pattern,
                        "usage_count": 1,
                        "success_rate": 1.0 if feedback_score and feedback_score > 0.8 else 0.0,
                        "last_used": datetime.now().isoformat()
                    }],
                    ids=[pattern_id]
                )
            except ValueError:  # Pattern already exists
                self._update_pattern_stats(pattern_id, feedback_score)

    def _extract_sql_patterns(self, sql: str) -> List[str]:
        """Extract common SQL patterns from query."""
        patterns = []
        # Basic patterns
        if "SELECT" in sql.upper():
            patterns.append("SELECT pattern")
        if "JOIN" in sql.upper():
            patterns.append("JOIN pattern")
        if "WHERE" in sql.upper():
            patterns.append("WHERE pattern")
        if "GROUP BY" in sql.upper():
            patterns.append("GROUP BY pattern")
        if "HAVING" in sql.upper():
            patterns.append("HAVING pattern")
        if "ORDER BY" in sql.upper():
            patterns.append("ORDER BY pattern")
        
        # Advanced patterns
        if "WITH" in sql.upper():
            patterns.append("CTE pattern")
        if "CASE" in sql.upper():
            patterns.append("CASE pattern")
        if "WINDOW" in sql.upper() or "OVER" in sql.upper():
            patterns.append("Window function pattern")
            
        return patterns

    def _calculate_sql_complexity(self, sql: str) -> float:
        """Calculate SQL query complexity score."""
        score = 0.0
        # Basic complexity factors
        score += sql.upper().count("SELECT") * 0.5
        score += sql.upper().count("JOIN") * 1.0
        score += sql.upper().count("WHERE") * 0.3
        score += sql.upper().count("GROUP BY") * 0.7
        score += sql.upper().count("HAVING") * 0.8
        score += sql.upper().count("ORDER BY") * 0.2
        
        # Advanced complexity factors
        score += sql.upper().count("WITH") * 1.5
        score += sql.upper().count("CASE") * 0.8
        score += sql.upper().count("WINDOW") * 1.2
        score += sql.upper().count("OVER") * 1.0
        
        return score

    def get_advanced_analytics(self) -> Dict:
        """Get advanced analytics about system usage and performance."""
        queries = self.query_collection.get()
        training = self.training_collection.get()
        patterns = self.pattern_collection.get()
        
        # Time-based analysis
        now = datetime.now()
        week_ago = now - timedelta(days=7)
        month_ago = now - timedelta(days=30)
        
        recent_queries = [
            meta for meta in queries["metadatas"]
            if datetime.fromisoformat(meta["timestamp"]) > week_ago
        ]
        
        # Pattern analysis
        pattern_stats = self._analyze_patterns(patterns["metadatas"])
        
        # Complexity analysis
        complexity_stats = self._analyze_complexity(
            queries["metadatas"], training["metadatas"]
        )
        
        # Learning curve analysis
        learning_curve = self._analyze_learning_curve(queries["metadatas"])
        
        return {
            "recent_stats": {
                "queries_last_week": len(recent_queries),
                "success_rate_week": sum(1 for q in recent_queries if q["successful"]) / len(recent_queries) if recent_queries else 0,
                "avg_complexity_week": sum(q.get("complexity", 0) for q in recent_queries) / len(recent_queries) if recent_queries else 0
            },
            "pattern_stats": pattern_stats,
            "complexity_stats": complexity_stats,
            "learning_curve": learning_curve,
            "schema_coverage": self._analyze_schema_coverage()
        }

    def _analyze_patterns(self, pattern_metadatas: List[Dict]) -> Dict:
        """Analyze SQL patterns usage and success rates."""
        pattern_usage = Counter()
        pattern_success = {}
        
        for meta in pattern_metadatas:
            pattern = meta["pattern"]
            pattern_usage[pattern] += meta["usage_count"]
            pattern_success[pattern] = meta["success_rate"]
        
        return {
            "most_common_patterns": pattern_usage.most_common(5),
            "pattern_success_rates": pattern_success,
            "pattern_trends": self._calculate_pattern_trends(pattern_metadatas)
        }

    def _analyze_complexity(self, query_metadatas: List[Dict], 
                          training_metadatas: List[Dict]) -> Dict:
        """Analyze query complexity trends."""
        query_complexities = [meta.get("complexity", 0) for meta in query_metadatas]
        training_complexities = [meta.get("complexity", 0) for meta in training_metadatas]
        
        return {
            "avg_query_complexity": np.mean(query_complexities) if query_complexities else 0,
            "avg_training_complexity": np.mean(training_complexities) if training_complexities else 0,
            "complexity_distribution": np.percentile(query_complexities, [25, 50, 75]) if query_complexities else [0, 0, 0],
            "complexity_trend": self._calculate_complexity_trend(query_metadatas)
        }

    def _analyze_learning_curve(self, query_metadatas: List[Dict]) -> Dict:
        """Analyze system learning curve over time."""
        if not query_metadatas:
            return {"success_rate_trend": [], "complexity_trend": []}
            
        df = pd.DataFrame(query_metadatas)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")
        
        # Calculate rolling success rate
        df["success_rate"] = df["successful"].rolling(window=50, min_periods=1).mean()
        
        # Calculate rolling complexity
        df["avg_complexity"] = df["complexity"].rolling(window=50, min_periods=1).mean()
        
        return {
            "success_rate_trend": df[["timestamp", "success_rate"]].values.tolist(),
            "complexity_trend": df[["timestamp", "avg_complexity"]].values.tolist()
        }

    def _analyze_schema_coverage(self) -> Dict:
        """Analyze how well the schema is covered by queries."""
        schema_metadatas = self.schema_collection.get()["metadatas"]
        query_metadatas = self.query_collection.get()["metadatas"]
        
        table_usage = Counter()
        column_usage = Counter()
        
        for query in query_metadatas:
            sql = query["sql"].upper()
            for schema in schema_metadatas:
                table_name = schema["table_name"]
                if table_name.upper() in sql:
                    table_usage[table_name] += 1
                    
                schema_info = json.loads(schema["schema_info"])
                for column in schema_info.get("columns", {}):
                    if column.upper() in sql:
                        column_usage[f"{table_name}.{column}"] += 1
        
        return {
            "table_coverage": {
                table: count/len(query_metadatas)
                for table, count in table_usage.items()
            },
            "column_coverage": {
                column: count/len(query_metadatas)
                for column, count in column_usage.most_common(10)
            }
        }

    def get_learning_recommendations(self) -> List[Dict]:
        """Get recommendations for improving system performance."""
        analytics = self.get_advanced_analytics()
        
        recommendations = []
        
        # Analyze pattern coverage
        pattern_stats = analytics["pattern_stats"]
        for pattern, success_rate in pattern_stats["pattern_success_rates"].items():
            if success_rate < 0.8:
                recommendations.append({
                    "type": "pattern_improvement",
                    "pattern": pattern,
                    "current_success_rate": success_rate,
                    "suggestion": f"Need more training examples for {pattern}"
                })
        
        # Analyze schema coverage
        schema_coverage = analytics["schema_coverage"]
        for table, coverage in schema_coverage["table_coverage"].items():
            if coverage < 0.3:
                recommendations.append({
                    "type": "schema_coverage",
                    "table": table,
                    "current_coverage": coverage,
                    "suggestion": f"Need more queries involving table {table}"
                })
        
        # Analyze complexity progression
        complexity_stats = analytics["complexity_stats"]
        if complexity_stats["avg_query_complexity"] < complexity_stats["avg_training_complexity"]:
            recommendations.append({
                "type": "complexity_gap",
                "current_gap": complexity_stats["avg_training_complexity"] - complexity_stats["avg_query_complexity"],
                "suggestion": "System needs more complex query examples"
            })
        
        return recommendations

    def export_analytics_report(self) -> Dict:
        """Export comprehensive analytics report."""
        analytics = self.get_advanced_analytics()
        recommendations = self.get_learning_recommendations()
        
        return {
            "timestamp": datetime.now().isoformat(),
            "summary_metrics": {
                "total_queries": len(self.query_collection.get()["ids"]),
                "total_training_examples": len(self.training_collection.get()["ids"]),
                "total_patterns": len(self.pattern_collection.get()["ids"]),
                "overall_success_rate": analytics["recent_stats"]["success_rate_week"]
            },
            "detailed_analytics": analytics,
            "recommendations": recommendations,
            "system_health": self._calculate_system_health(analytics)
        }

    def _calculate_system_health(self, analytics: Dict) -> Dict:
        """Calculate overall system health metrics."""
        return {
            "success_rate_health": "good" if analytics["recent_stats"]["success_rate_week"] > 0.8 else "needs_improvement",
            "pattern_coverage": "good" if len(analytics["pattern_stats"]["most_common_patterns"]) > 10 else "needs_improvement",
            "schema_coverage": "good" if min(analytics["schema_coverage"]["table_coverage"].values()) > 0.3 else "needs_improvement",
            "learning_progress": "good" if analytics["learning_curve"]["success_rate_trend"][-1][1] > analytics["learning_curve"]["success_rate_trend"][0][1] else "needs_improvement"
        }
