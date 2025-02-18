*** Settings ***
Documentation     Keywords for vector store testing
Library           OperatingSystem
Library           Collections
Library           DateTime
Library           adpa.knowledge.enhanced_vectorstore.EnhancedVectorStore
Library           adpa.knowledge.vectorstore.KnowledgeBase

*** Keywords ***
Create Vector Store
    [Arguments]    ${store_type}    ${persist_dir}=${EMPTY}    ${collection_name}=${EMPTY}    ${index_type}=${EMPTY}    ${consistency_level}=${EMPTY}
    ${config}=    Create Dictionary
    ...    store_type=${store_type}
    ...    embedding_type=openai
    ...    persist_directory=${persist_dir}
    ...    embedding_model=text-embedding-ada-002
    ...    chunk_size=1000
    ...    chunk_overlap=200
    
    IF    '${collection_name}' != '${EMPTY}'
        Set To Dictionary    ${config}    collection_name=${collection_name}
    END
    
    IF    '${index_type}' != '${EMPTY}'
        Set To Dictionary    ${config}    index_type=${index_type}
    END
    
    IF    '${consistency_level}' != '${EMPTY}'
        Set To Dictionary    ${config}    consistency_level=${consistency_level}
    END
    
    ${store}=    Create Enhanced Vector Store    ${config}
    Set Test Variable    ${VECTOR_STORE}    ${store}

Add Document To Store
    [Arguments]    ${content}    ${doc_id}    ${metadata}=${EMPTY}
    ${meta}=    Run Keyword If    '${metadata}' == '${EMPTY}'
    ...    Create Dictionary    doc_id=${doc_id}
    ...    ELSE    Set Variable    ${metadata}
    ${VECTOR_STORE}.add_documents    ${content}    metadata=${meta}

Search Documents
    [Arguments]    ${query}    ${k}=5
    ${results}=    ${VECTOR_STORE}.similarity_search    ${query}    k=${k}
    [Return]    ${results}

Search Documents With Filter
    [Arguments]    ${query}    ${k}=5    &{filter_dict}
    ${results}=    ${VECTOR_STORE}.similarity_search    
    ...    ${query}    
    ...    k=${k}    
    ...    filter=${filter_dict}
    [Return]    ${results}

Delete Document From Store
    [Arguments]    ${doc_id}
    ${VECTOR_STORE}.delete_document    ${doc_id}

Delete Multiple Documents
    [Arguments]    @{doc_ids}
    FOR    ${doc_id}    IN    @{doc_ids}
        Delete Document From Store    ${doc_id}
    END

Cleanup Vector Store
    [Arguments]    ${store_type}
    Run Keyword If    '${store_type}' == 'chroma'    Remove Directory    ${CHROMA_DIR}    recursive=True
    Run Keyword If    '${store_type}' == 'faiss'     Remove Directory    ${FAISS_DIR}     recursive=True
    Run Keyword If    '${store_type}' == 'milvus'    Delete Milvus Collection

Delete Milvus Collection
    ${VECTOR_STORE}.delete_collection

Reload Vector Store
    [Arguments]    ${store_type}    ${persist_dir}
    Create Vector Store    ${store_type}    ${persist_dir}

Create Partitioned Milvus Store
    [Arguments]    ${collection_name}    @{partition_names}
    Create Vector Store    milvus    collection_name=${collection_name}
    FOR    ${partition}    IN    @{partition_names}
        ${VECTOR_STORE}.create_partition    ${partition}
    END

Add Documents To Partition
    [Arguments]    ${partition_name}    @{documents}
    FOR    ${index}    ${doc}    IN ENUMERATE    @{documents}
        ${metadata}=    Create Dictionary    
        ...    doc_id=p${partition_name}_${index}    
        ...    partition=${partition_name}
        Add Document To Store    ${doc}    p${partition_name}_${index}    ${metadata}
    END

Search In Partition
    [Arguments]    ${partition_name}    ${query}    ${k}=5
    ${results}=    ${VECTOR_STORE}.similarity_search    
    ...    ${query}    
    ...    k=${k}    
    ...    partition_names=["${partition_name}"]
    [Return]    ${results}

Measure Store Performance
    [Arguments]    ${store_type}    ${num_docs}
    Create Vector Store    ${store_type}
    
    # Measure insertion time
    ${start_time}=    Get Time    epoch
    ${docs}=    Generate Test Documents    ${num_docs}
    Add Multiple Documents    @{docs}
    ${end_time}=    Get Time    epoch
    ${insert_time}=    Evaluate    ${end_time} - ${start_time}
    
    # Measure search time
    ${start_time}=    Get Time    epoch
    ${queries}=    Create List    
    ...    artificial intelligence    
    ...    machine learning    
    ...    neural networks
    FOR    ${query}    IN    @{queries}
        Search Documents    ${query}    k=10
    END
    ${end_time}=    Get Time    epoch
    ${search_time}=    Evaluate    ${end_time} - ${start_time}
    
    # Calculate metrics
    ${avg_insert_per_doc}=    Evaluate    ${insert_time} / ${num_docs}
    ${avg_search_time}=    Evaluate    ${search_time} / len($queries)
    
    ${metrics}=    Create Dictionary
    ...    total_docs=${num_docs}
    ...    total_insert_time=${insert_time}
    ...    avg_insert_per_doc=${avg_insert_per_doc}
    ...    total_search_time=${search_time}
    ...    avg_search_time=${avg_search_time}
    
    [Return]    ${metrics}

Setup Vector Store Tests
    Create Directory    ${TEST_DATA_DIR}
    Create Directory    ${CHROMA_DIR}
    Create Directory    ${FAISS_DIR}
    Set Environment Variable    OPENAI_API_KEY    your_test_api_key

Cleanup Vector Store Tests
    Remove Directory    ${TEST_DATA_DIR}    recursive=True
