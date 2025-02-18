from typing import Optional, List

from pygeai.assistant.rag.responses import DocumentListResponse
from pygeai.core.base.mappers import ModelMapper
from pygeai.core.base.models import ChatVariable, \
    ChatVariableList
from pygeai.assistant.rag.models import LlmOptions, Search, RetrieverOptions, EmbeddingsOptions, IngestionOptions, \
    SearchOptions, ChildOptions, ChildDocumentOptions, ChunkOptions, IndexOptions, RAGAssistant, Document, \
    DocumentMetadata


class RAGAssistantMapper(ModelMapper):

    @classmethod
    def map_to_rag_assistant(cls, data: dict) -> RAGAssistant:
        welcome_data = cls.map_to_welcome_data(data) if 'welcomeData' in data else None
        llm_settings = cls.map_to_llm_settings(data.get('llmSettings')) if 'llmSettings' in data else None
        search_options = cls.map_to_search_options(data.get('searchOptions')) if 'searchOptions' in data else None
        index_options = cls.map_to_index_options(data.get('indexOptions')) if 'indexOptions' in data else None

        return RAGAssistant(
            name=data.get("name"),
            type="rag",
            status=data.get("status"),
            description=data.get("description"),
            prompt=data.get("prompt"),
            template=data.get('template'),
            search_options=search_options,
            index_options=index_options,
            welcome_data=welcome_data,
            llm_settings=llm_settings
        )

    @classmethod
    def map_to_search_options(cls, data: dict) -> SearchOptions:
        """
        Maps a dictionary to a `SearchOptions` object.

        :param data: dict - The dictionary containing search options details.
        :return: SearchOptions - The mapped `SearchOptions` object.
        """
        return SearchOptions(
            history_count=data.get("historyCount"),
            llm=cls.map_to_llm_options(data.get("llm")),
            search=cls.map_to_search(data.get("search")),
            retriever=cls.map_to_retriever_options(data.get("retriever")),
            chain=data.get('chain'),
            embeddings=cls.map_to_embeddings(data.get('embeddings')),
            ingestion=cls.map_to_ingestion(data.get('ingestion')),
            options=data.get('options'),
            rerank=data.get('rerank'),
            variables=cls.map_to_variable_list(data.get('variables')),
            vector_store=data.get('vector_store'),
        )

    @classmethod
    def map_to_llm_options(cls, data: dict) -> LlmOptions:
        return LlmOptions(
            cache=data.get("cache"),
            frequency_penalty=data.get("frequencyPenalty"),
            max_tokens=data.get("maxTokens"),
            model_name=data.get("modelName"),
            n=data.get("n"),
            presence_penalty=data.get("presencePenalty"),
            provider=data.get("provider"),
            stream=data.get("stream"),
            temperature=data.get("temperature"),
            topP=data.get("topP"),
            type=data.get("type", ""),
            verbose=data.get("verbose")
        )

    @classmethod
    def map_to_search(cls, data: dict) -> Search:
        return Search(
            k=data.get("k"),
            type=data.get("type", "similarity"),
            fetch_k=data.get("fetchK"),
            lambda_=data.get("lambda"),
            prompt=data.get("prompt"),
            return_source_documents=data.get("returnSourceDocuments"),
            score_threshold=data.get("scoreThreshold"),
            template=data.get("template")
        )

    @classmethod
    def map_to_retriever_options(cls, data: dict) -> RetrieverOptions:
        return RetrieverOptions(
            type=data.get("type"),
            search_type=data.get("searchType", "similarity"),
            step=data.get("step", "all"),
            prompt=data.get("prompt")
        )

    @classmethod
    def map_to_index_options(cls, data: dict) -> IndexOptions:
        """
        Maps a dictionary to an `IndexOptions` object.

        :param data: dict - The dictionary containing index options details.
        :return: IndexOptions - The mapped `IndexOptions` object.
        """
        return IndexOptions(
            chunks=cls.map_to_chunk_options(data.get("chunks")),
            use_parent_document=data.get("useParentDocument", False),
            child_document=cls.map_to_child_document_options(data.get("childDocument"))
            if data.get("useParentDocument") else None
        )

    @classmethod
    def map_to_chunk_options(cls, data: dict) -> ChunkOptions:
        return ChunkOptions(
            chunk_overlap=data.get("chunkOverlap"),
            chunk_size=data.get("chunkSize")
        )

    @classmethod
    def map_to_child_document_options(cls, data: dict) -> ChildDocumentOptions:
        return ChildDocumentOptions(
            child_k=data.get("childK"),
            child=cls.map_to_child_options(data.get("child"))
        )

    @classmethod
    def map_to_child_options(cls, data: dict) -> ChildOptions:
        return ChildOptions(
            chunk_size=data.get("chunkSize"),
            chunk_overlap=data.get("chunkOverlap"),
            content_processing=data.get("contentProcessing", "")
        )

    @classmethod
    def map_to_embeddings(cls, data: dict) -> Optional[EmbeddingsOptions]:
        """
        Maps a dictionary to an `EmbeddingsOptions` object.

        :param data: dict - The dictionary containing embeddings options details.
        :return: EmbeddingsOptions - The mapped `EmbeddingsOptions` object.
        """
        return EmbeddingsOptions(
            dimensions=data.get('dimensions'),
            model_name=data.get('modelName'),
            provider=data.get('provider'),
            use_proxy=data.get('useProxy')
        )

    @classmethod
    def map_to_ingestion(cls, data: dict) -> Optional[IngestionOptions]:
        """
        Maps a dictionary to an `IngestionOptions` object.

        :param data: dict - The dictionary containing ingestion options details.
        :return: IngestionOptions - The mapped `IngestionOptions` object.
        """
        return IngestionOptions(
            geai_options=data.get('geaiOptions'),
            llama_parse_options=data.get('llamaParseOptions'),
            provider=data.get('provider')
        )

    @classmethod
    def map_to_variable_list(cls, data: list) -> Optional[ChatVariableList]:
        """
        Maps a list of dictionaries to a `ChatVariableList` object.

        :param data: list - The list containing chat variable details.
        :return: ChatVariableList - The mapped `ChatVariableList` object.
        """
        variables = list()
        for variable in data:
            for k, v in variable.items():
                variables.append(
                    ChatVariable(
                        key=k,
                        value=v
                    )
                )

        return ChatVariableList(variables=variables)

    @classmethod
    def map_to_document_list_response(cls, data: dict) -> DocumentListResponse:
        documents = cls.map_to_document_list(data)
        count = data.get('count')

        return DocumentListResponse(
            count=count,
            documents=documents
        )

    @classmethod
    def map_to_document_list(cls, data: dict) -> list[Document]:
        document_list = list()
        documents = data.get("documents")
        if documents is not None and any(documents):
            for document_data in documents:
                document = cls.map_to_document(document_data)
                document_list.append(document)

        return document_list

    @classmethod
    def map_to_document(cls, data: dict) -> Document:
        metadata = cls.map_to_document_metadata_list(data)

        return Document(
            id=data.get('id'),
            chunks=data.get('chunks'),
            extension=data.get('extension'),
            index_status=data.get('indexStatus'),
            metadata=metadata,
            timestamp=data.get('timestamp'),
            url=data.get('url'),
        )

    @classmethod
    def map_to_document_metadata_list(cls, data: dict) -> List[DocumentMetadata]:
        metadata_list = list()
        metadata = data.get('metadata')
        if metadata is not None and any(metadata):
            for metadata_data in metadata:
                new_metadata = cls.map_to_document_metadata(metadata_data)
                metadata_list.append(new_metadata)

        return metadata_list

    @classmethod
    def map_to_document_metadata(cls, data: dict) -> DocumentMetadata:
        return DocumentMetadata(
            key=data.get('key'),
            value=data.get('value')
        )

