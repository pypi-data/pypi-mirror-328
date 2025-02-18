*** Settings ***
Documentation     Test suite for vector store functionality
Resource          resources/common.robot
Resource          resources/vector_store_keywords.robot
Library           OperatingSystem
Library           Collections
Library           DateTime
Suite Setup       Setup Vector Store Tests
Suite Teardown    Cleanup Vector Store Tests

*** Variables ***
${TEST_DATA_DIR}    ${CURDIR}/test_data/vector_stores
${SAMPLE_TEXT}      This is a sample document for testing vector stores.
${QUERY_TEXT}       sample document
${CHROMA_DIR}       ${TEST_DATA_DIR}/chroma_store
${FAISS_DIR}        ${TEST_DATA_DIR}/faiss_store
${MILVUS_HOST}      localhost
${MILVUS_PORT}      19530
@{TEST_DOCUMENTS}    
...    This is the first test document about artificial intelligence.
...    The second document discusses machine learning applications.
...    Document three covers natural language processing.
...    The fourth document is about vector databases and similarity search.
...    Document five explains neural networks and deep learning.

*** Test Cases ***
Chroma Basic Operations
    [Documentation]    Test basic Chroma vector store operations
    [Tags]    vector-store    chroma    basic
    Create Vector Store    chroma    ${CHROMA_DIR}
    Add Document To Store    ${SAMPLE_TEXT}    doc1
    ${results}=    Search Documents    ${QUERY_TEXT}    k=1
    Length Should Be    ${results}    1
    Should Contain    ${results}[0]    ${SAMPLE_TEXT}
    Delete Document From Store    doc1
    Cleanup Vector Store    chroma

Chroma Batch Operations
    [Documentation]    Test Chroma batch operations and metadata filtering
    [Tags]    vector-store    chroma    batch
    Create Vector Store    chroma    ${CHROMA_DIR}
    Add Multiple Documents    ${TEST_DOCUMENTS}
    ${results}=    Search Documents With Filter    artificial intelligence    category=AI    k=2
    Length Should Be    ${results}    2
    Delete Multiple Documents    batch1    batch2
    Cleanup Vector Store    chroma

Chroma Persistence Test
    [Documentation]    Test Chroma persistence across sessions
    [Tags]    vector-store    chroma    persistence
    Create Vector Store    chroma    ${CHROMA_DIR}
    Add Document To Store    ${SAMPLE_TEXT}    persist_doc
    Reload Vector Store    chroma    ${CHROMA_DIR}
    ${results}=    Search Documents    ${QUERY_TEXT}    k=1
    Length Should Be    ${results}    1
    Cleanup Vector Store    chroma

FAISS Basic Operations
    [Documentation]    Test basic FAISS vector store operations
    [Tags]    vector-store    faiss    basic
    Create Vector Store    faiss    ${FAISS_DIR}
    Add Document To Store    ${SAMPLE_TEXT}    doc1
    ${results}=    Search Documents    ${QUERY_TEXT}    k=1
    Length Should Be    ${results}    1
    Should Contain    ${results}[0]    ${SAMPLE_TEXT}
    Delete Document From Store    doc1
    Cleanup Vector Store    faiss

FAISS Advanced Search
    [Documentation]    Test FAISS advanced search capabilities
    [Tags]    vector-store    faiss    advanced
    Create Vector Store    faiss    ${FAISS_DIR}
    Add Multiple Documents    ${TEST_DOCUMENTS}
    ${results1}=    Search Documents    neural networks    k=2
    ${results2}=    Search Documents    machine learning    k=2
    Lists Should Not Be Equal    ${results1}    ${results2}
    Cleanup Vector Store    faiss

FAISS Index Types Test
    [Documentation]    Test different FAISS index types
    [Tags]    vector-store    faiss    index
    Test FAISS Index Type    IndexFlatIP    100
    Test FAISS Index Type    IndexIVFFlat    1000

Milvus Basic Operations
    [Documentation]    Test basic Milvus vector store operations
    [Tags]    vector-store    milvus    basic
    Create Vector Store    milvus    collection_name=test_collection
    Add Document To Store    ${SAMPLE_TEXT}    doc1
    ${results}=    Search Documents    ${QUERY_TEXT}    k=1
    Length Should Be    ${results}    1
    Should Contain    ${results}[0]    ${SAMPLE_TEXT}
    Delete Document From Store    doc1
    Cleanup Vector Store    milvus

Milvus Partition Test
    [Documentation]    Test Milvus partitioning
    [Tags]    vector-store    milvus    partition
    Create Partitioned Milvus Store    test_collection    partition1    partition2
    Add Documents To Partition    partition1    ${TEST_DOCUMENTS}[0:2]
    Add Documents To Partition    partition2    ${TEST_DOCUMENTS}[2:4]
    ${results1}=    Search In Partition    partition1    artificial intelligence    k=1
    ${results2}=    Search In Partition    partition2    natural language    k=1
    Lists Should Not Be Equal    ${results1}    ${results2}
    Cleanup Vector Store    milvus

Milvus Consistency Test
    [Documentation]    Test Milvus consistency levels
    [Tags]    vector-store    milvus    consistency
    Test Milvus Consistency    Strong
    Test Milvus Consistency    Bounded
    Test Milvus Consistency    Session

Vector Store Performance Comparison
    [Documentation]    Compare performance across vector stores
    [Tags]    vector-store    performance    comparison
    [Template]    Compare Store Performance
    chroma    faiss     100
    chroma    milvus    100
    faiss     milvus    100

Vector Store Stress Test
    [Documentation]    Stress test vector stores with large operations
    [Tags]    vector-store    stress
    [Template]    Stress Test Store
    chroma    1000    10
    faiss     1000    10
    milvus    1000    10

*** Keywords ***
Add Multiple Documents
    [Arguments]    @{documents}
    FOR    ${index}    ${doc}    IN ENUMERATE    @{documents}
        ${metadata}=    Create Dictionary    
        ...    doc_id=batch${index}    
        ...    category=AI    
        ...    timestamp=${GET_TIME}
        Add Document To Store    ${doc}    batch${index}    ${metadata}
    END

Test FAISS Index Type
    [Arguments]    ${index_type}    ${num_docs}
    Create Vector Store    faiss    ${FAISS_DIR}    index_type=${index_type}
    ${start_time}=    Get Time    epoch
    Add Multiple Documents    @{TEST_DOCUMENTS}
    ${end_time}=    Get Time    epoch
    ${index_time}=    Evaluate    ${end_time} - ${start_time}
    Log    Index build time (${index_type}): ${index_time}s
    Cleanup Vector Store    faiss

Test Milvus Consistency
    [Arguments]    ${consistency_level}
    Create Vector Store    milvus    
    ...    collection_name=test_consistency    
    ...    consistency_level=${consistency_level}
    Add Document To Store    ${SAMPLE_TEXT}    doc1
    ${results}=    Search Documents    ${QUERY_TEXT}    k=1
    Length Should Be    ${results}    1
    Cleanup Vector Store    milvus

Compare Store Performance
    [Arguments]    ${store1}    ${store2}    ${num_docs}
    ${store1_metrics}=    Measure Store Performance    ${store1}    ${num_docs}
    ${store2_metrics}=    Measure Store Performance    ${store2}    ${num_docs}
    Log    Performance Comparison:
    Log    ${store1}: ${store1_metrics}
    Log    ${store2}: ${store2_metrics}

Stress Test Store
    [Arguments]    ${store_type}    ${num_docs}    ${num_queries}
    Create Vector Store    ${store_type}
    ${docs}=    Generate Test Documents    ${num_docs}
    Add Multiple Documents    @{docs}
    FOR    ${i}    IN RANGE    ${num_queries}
        ${query}=    Generate Random Query
        Search Documents    ${query}    k=10
    END
    Cleanup Vector Store    ${store_type}

Generate Test Documents
    [Arguments]    ${count}
    @{docs}=    Create List
    FOR    ${i}    IN RANGE    ${count}
        ${doc}=    Set Variable    Test document ${i} with random content for stress testing.
        Append To List    ${docs}    ${doc}
    END
    [Return]    ${docs}

Generate Random Query
    ${queries}=    Create List    
    ...    artificial intelligence    
    ...    machine learning    
    ...    neural networks    
    ...    deep learning    
    ...    natural language processing
    ${query}=    Evaluate    random.choice($queries)    random
    [Return]    ${query}
