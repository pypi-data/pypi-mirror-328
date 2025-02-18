# coding: utf-8

# flake8: noqa
"""
    Rapidata.Dataset

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from rapidata.api_client.models.ab_test_selection import AbTestSelection
from rapidata.api_client.models.ab_test_selection_a_inner import AbTestSelectionAInner
from rapidata.api_client.models.add_campaign_artifact_result import AddCampaignArtifactResult
from rapidata.api_client.models.add_campaign_model import AddCampaignModel
from rapidata.api_client.models.add_validation_rapid_model import AddValidationRapidModel
from rapidata.api_client.models.add_validation_rapid_model_payload import AddValidationRapidModelPayload
from rapidata.api_client.models.add_validation_rapid_model_truth import AddValidationRapidModelTruth
from rapidata.api_client.models.add_validation_rapid_result import AddValidationRapidResult
from rapidata.api_client.models.add_validation_text_rapid_model import AddValidationTextRapidModel
from rapidata.api_client.models.age_group import AgeGroup
from rapidata.api_client.models.age_user_filter_model import AgeUserFilterModel
from rapidata.api_client.models.aggregator_type import AggregatorType
from rapidata.api_client.models.attach_category_rapid_blueprint import AttachCategoryRapidBlueprint
from rapidata.api_client.models.attach_category_result import AttachCategoryResult
from rapidata.api_client.models.attach_category_truth import AttachCategoryTruth
from rapidata.api_client.models.base_error import BaseError
from rapidata.api_client.models.bounding_box_payload import BoundingBoxPayload
from rapidata.api_client.models.bounding_box_rapid_blueprint import BoundingBoxRapidBlueprint
from rapidata.api_client.models.bounding_box_result import BoundingBoxResult
from rapidata.api_client.models.bounding_box_truth import BoundingBoxTruth
from rapidata.api_client.models.box_shape import BoxShape
from rapidata.api_client.models.campaign_artifact_model import CampaignArtifactModel
from rapidata.api_client.models.campaign_query_model import CampaignQueryModel
from rapidata.api_client.models.campaign_query_model_paged_result import CampaignQueryModelPagedResult
from rapidata.api_client.models.campaign_status import CampaignStatus
from rapidata.api_client.models.campaign_user_filter_model import CampaignUserFilterModel
from rapidata.api_client.models.capped_selection import CappedSelection
from rapidata.api_client.models.classification_metadata import ClassificationMetadata
from rapidata.api_client.models.classification_metadata_filter_config import ClassificationMetadataFilterConfig
from rapidata.api_client.models.classification_metadata_model import ClassificationMetadataModel
from rapidata.api_client.models.classify_payload import ClassifyPayload
from rapidata.api_client.models.clients_query_result import ClientsQueryResult
from rapidata.api_client.models.clients_query_result_paged_result import ClientsQueryResultPagedResult
from rapidata.api_client.models.clone_dataset_model import CloneDatasetModel
from rapidata.api_client.models.clone_order_model import CloneOrderModel
from rapidata.api_client.models.clone_order_result import CloneOrderResult
from rapidata.api_client.models.compare_match_status import CompareMatchStatus
from rapidata.api_client.models.compare_payload import ComparePayload
from rapidata.api_client.models.compare_rapid_blueprint import CompareRapidBlueprint
from rapidata.api_client.models.compare_result import CompareResult
from rapidata.api_client.models.compare_truth import CompareTruth
from rapidata.api_client.models.compare_workflow_config import CompareWorkflowConfig
from rapidata.api_client.models.compare_workflow_config_model import CompareWorkflowConfigModel
from rapidata.api_client.models.compare_workflow_config_model_pair_maker_config import CompareWorkflowConfigModelPairMakerConfig
from rapidata.api_client.models.compare_workflow_config_pair_maker_config import CompareWorkflowConfigPairMakerConfig
from rapidata.api_client.models.compare_workflow_model import CompareWorkflowModel
from rapidata.api_client.models.compare_workflow_model1 import CompareWorkflowModel1
from rapidata.api_client.models.compare_workflow_model1_pair_maker_information import CompareWorkflowModel1PairMakerInformation
from rapidata.api_client.models.compare_workflow_model1_referee import CompareWorkflowModel1Referee
from rapidata.api_client.models.compare_workflow_model_pair_maker_config import CompareWorkflowModelPairMakerConfig
from rapidata.api_client.models.conditional_validation_selection import ConditionalValidationSelection
from rapidata.api_client.models.coordinate import Coordinate
from rapidata.api_client.models.count_classification_metadata_filter_config import CountClassificationMetadataFilterConfig
from rapidata.api_client.models.count_metadata import CountMetadata
from rapidata.api_client.models.count_metadata_model import CountMetadataModel
from rapidata.api_client.models.country_user_filter_model import CountryUserFilterModel
from rapidata.api_client.models.create_bridge_token_result import CreateBridgeTokenResult
from rapidata.api_client.models.create_client_model import CreateClientModel
from rapidata.api_client.models.create_client_result import CreateClientResult
from rapidata.api_client.models.create_complex_order_model import CreateComplexOrderModel
from rapidata.api_client.models.create_complex_order_model_pipeline import CreateComplexOrderModelPipeline
from rapidata.api_client.models.create_complex_order_result import CreateComplexOrderResult
from rapidata.api_client.models.create_dataset_artifact_model import CreateDatasetArtifactModel
from rapidata.api_client.models.create_dataset_artifact_model_dataset import CreateDatasetArtifactModelDataset
from rapidata.api_client.models.create_demographic_rapid_model import CreateDemographicRapidModel
from rapidata.api_client.models.create_empty_validation_set_result import CreateEmptyValidationSetResult
from rapidata.api_client.models.create_order_model import CreateOrderModel
from rapidata.api_client.models.create_order_model_referee import CreateOrderModelReferee
from rapidata.api_client.models.create_order_model_user_filters_inner import CreateOrderModelUserFiltersInner
from rapidata.api_client.models.create_order_model_workflow import CreateOrderModelWorkflow
from rapidata.api_client.models.create_order_result import CreateOrderResult
from rapidata.api_client.models.create_simple_pipeline_model import CreateSimplePipelineModel
from rapidata.api_client.models.create_simple_pipeline_model_artifacts_inner import CreateSimplePipelineModelArtifactsInner
from rapidata.api_client.models.create_simple_pipeline_model_pipeline_steps_inner import CreateSimplePipelineModelPipelineStepsInner
from rapidata.api_client.models.create_unsupported_order_model import CreateUnsupportedOrderModel
from rapidata.api_client.models.custom_user_filter_model import CustomUserFilterModel
from rapidata.api_client.models.datapoint import Datapoint
from rapidata.api_client.models.datapoint_asset import DatapointAsset
from rapidata.api_client.models.datapoint_get_by_id_get200_response import DatapointGetByIdGet200Response
from rapidata.api_client.models.datapoint_metadata_model import DatapointMetadataModel
from rapidata.api_client.models.datapoint_metadata_model_metadata_inner import DatapointMetadataModelMetadataInner
from rapidata.api_client.models.datapoint_model import DatapointModel
from rapidata.api_client.models.datapoint_model_asset import DatapointModelAsset
from rapidata.api_client.models.dataset_artifact_model import DatasetArtifactModel
from rapidata.api_client.models.dataset_evaluation_step_model import DatasetEvaluationStepModel
from rapidata.api_client.models.demographic_metadata_model import DemographicMetadataModel
from rapidata.api_client.models.demographic_selection import DemographicSelection
from rapidata.api_client.models.early_stopping_referee_model import EarlyStoppingRefereeModel
from rapidata.api_client.models.empty_validation_truth import EmptyValidationTruth
from rapidata.api_client.models.evaluation_workflow_config import EvaluationWorkflowConfig
from rapidata.api_client.models.evaluation_workflow_model import EvaluationWorkflowModel
from rapidata.api_client.models.feature_flag import FeatureFlag
from rapidata.api_client.models.feature_flag_model import FeatureFlagModel
from rapidata.api_client.models.feedback_model import FeedbackModel
from rapidata.api_client.models.file_artifact_model import FileArtifactModel
from rapidata.api_client.models.file_asset import FileAsset
from rapidata.api_client.models.file_asset_metadata_inner import FileAssetMetadataInner
from rapidata.api_client.models.file_asset_model import FileAssetModel
from rapidata.api_client.models.file_asset_model1 import FileAssetModel1
from rapidata.api_client.models.file_asset_model1_metadata_inner import FileAssetModel1MetadataInner
from rapidata.api_client.models.file_asset_model2 import FileAssetModel2
from rapidata.api_client.models.file_asset_model_metadata_inner import FileAssetModelMetadataInner
from rapidata.api_client.models.filter import Filter
from rapidata.api_client.models.filter_operator import FilterOperator
from rapidata.api_client.models.free_text_payload import FreeTextPayload
from rapidata.api_client.models.free_text_rapid_blueprint import FreeTextRapidBlueprint
from rapidata.api_client.models.free_text_result import FreeTextResult
from rapidata.api_client.models.gender import Gender
from rapidata.api_client.models.gender_user_filter_model import GenderUserFilterModel
from rapidata.api_client.models.get_available_validation_sets_result import GetAvailableValidationSetsResult
from rapidata.api_client.models.get_compare_ab_summary_result import GetCompareAbSummaryResult
from rapidata.api_client.models.get_compare_workflow_results_model import GetCompareWorkflowResultsModel
from rapidata.api_client.models.get_compare_workflow_results_result import GetCompareWorkflowResultsResult
from rapidata.api_client.models.get_compare_workflow_results_result_asset import GetCompareWorkflowResultsResultAsset
from rapidata.api_client.models.get_compare_workflow_results_result_paged_result import GetCompareWorkflowResultsResultPagedResult
from rapidata.api_client.models.get_datapoints_by_dataset_id_result import GetDatapointsByDatasetIdResult
from rapidata.api_client.models.get_dataset_by_id_result import GetDatasetByIdResult
from rapidata.api_client.models.get_order_by_id_result import GetOrderByIdResult
from rapidata.api_client.models.get_pipeline_by_id_result import GetPipelineByIdResult
from rapidata.api_client.models.get_pipeline_by_id_result_artifacts_value import GetPipelineByIdResultArtifactsValue
from rapidata.api_client.models.get_public_orders_result import GetPublicOrdersResult
from rapidata.api_client.models.get_simple_workflow_results_model import GetSimpleWorkflowResultsModel
from rapidata.api_client.models.get_simple_workflow_results_result import GetSimpleWorkflowResultsResult
from rapidata.api_client.models.get_simple_workflow_results_result_paged_result import GetSimpleWorkflowResultsResultPagedResult
from rapidata.api_client.models.get_validation_set_by_id_result import GetValidationSetByIdResult
from rapidata.api_client.models.get_workflow_by_id_result import GetWorkflowByIdResult
from rapidata.api_client.models.get_workflow_by_id_result_workflow import GetWorkflowByIdResultWorkflow
from rapidata.api_client.models.get_workflow_progress_result import GetWorkflowProgressResult
from rapidata.api_client.models.i_workflow_model_paged_result import IWorkflowModelPagedResult
from rapidata.api_client.models.identity_read_bridge_token_get202_response import IdentityReadBridgeTokenGet202Response
from rapidata.api_client.models.image_dimension_metadata import ImageDimensionMetadata
from rapidata.api_client.models.image_dimension_metadata_model import ImageDimensionMetadataModel
from rapidata.api_client.models.import_from_file_result import ImportFromFileResult
from rapidata.api_client.models.import_validation_set_from_file_result import ImportValidationSetFromFileResult
from rapidata.api_client.models.labeling_selection import LabelingSelection
from rapidata.api_client.models.language_user_filter_model import LanguageUserFilterModel
from rapidata.api_client.models.line import Line
from rapidata.api_client.models.line_payload import LinePayload
from rapidata.api_client.models.line_point import LinePoint
from rapidata.api_client.models.line_rapid_blueprint import LineRapidBlueprint
from rapidata.api_client.models.line_result import LineResult
from rapidata.api_client.models.line_truth import LineTruth
from rapidata.api_client.models.locate_box_truth import LocateBoxTruth
from rapidata.api_client.models.locate_coordinate import LocateCoordinate
from rapidata.api_client.models.locate_payload import LocatePayload
from rapidata.api_client.models.locate_rapid_blueprint import LocateRapidBlueprint
from rapidata.api_client.models.locate_result import LocateResult
from rapidata.api_client.models.location_metadata import LocationMetadata
from rapidata.api_client.models.location_metadata_exists_filter_config import LocationMetadataExistsFilterConfig
from rapidata.api_client.models.location_metadata_model import LocationMetadataModel
from rapidata.api_client.models.logic_operator import LogicOperator
from rapidata.api_client.models.metadata_visibilities import MetadataVisibilities
from rapidata.api_client.models.multi_asset import MultiAsset
from rapidata.api_client.models.multi_asset_model import MultiAssetModel
from rapidata.api_client.models.multi_asset_model1 import MultiAssetModel1
from rapidata.api_client.models.multi_asset_model1_assets_inner import MultiAssetModel1AssetsInner
from rapidata.api_client.models.multi_asset_model2 import MultiAssetModel2
from rapidata.api_client.models.naive_referee_config import NaiveRefereeConfig
from rapidata.api_client.models.naive_referee_model import NaiveRefereeModel
from rapidata.api_client.models.named_classification import NamedClassification
from rapidata.api_client.models.named_entity_payload import NamedEntityPayload
from rapidata.api_client.models.named_entity_rapid_blueprint import NamedEntityRapidBlueprint
from rapidata.api_client.models.named_entity_result import NamedEntityResult
from rapidata.api_client.models.named_entity_truth import NamedEntityTruth
from rapidata.api_client.models.never_ending_referee_config import NeverEndingRefereeConfig
from rapidata.api_client.models.newsletter_model import NewsletterModel
from rapidata.api_client.models.not_available_yet_result import NotAvailableYetResult
from rapidata.api_client.models.null_asset import NullAsset
from rapidata.api_client.models.null_asset_model import NullAssetModel
from rapidata.api_client.models.null_asset_model1 import NullAssetModel1
from rapidata.api_client.models.null_asset_model2 import NullAssetModel2
from rapidata.api_client.models.online_pair_maker_config import OnlinePairMakerConfig
from rapidata.api_client.models.online_pair_maker_config_model import OnlinePairMakerConfigModel
from rapidata.api_client.models.online_pair_maker_information import OnlinePairMakerInformation
from rapidata.api_client.models.order_model import OrderModel
from rapidata.api_client.models.order_model_paged_result import OrderModelPagedResult
from rapidata.api_client.models.order_state import OrderState
from rapidata.api_client.models.original_filename_metadata import OriginalFilenameMetadata
from rapidata.api_client.models.original_filename_metadata_model import OriginalFilenameMetadataModel
from rapidata.api_client.models.page_info import PageInfo
from rapidata.api_client.models.pipeline_id_workflow_put_request import PipelineIdWorkflowPutRequest
from rapidata.api_client.models.polygon_payload import PolygonPayload
from rapidata.api_client.models.polygon_rapid_blueprint import PolygonRapidBlueprint
from rapidata.api_client.models.polygon_result import PolygonResult
from rapidata.api_client.models.polygon_truth import PolygonTruth
from rapidata.api_client.models.pre_arranged_pair_maker_config import PreArrangedPairMakerConfig
from rapidata.api_client.models.pre_arranged_pair_maker_config_model import PreArrangedPairMakerConfigModel
from rapidata.api_client.models.pre_arranged_pair_maker_information import PreArrangedPairMakerInformation
from rapidata.api_client.models.preliminary_download_model import PreliminaryDownloadModel
from rapidata.api_client.models.preliminary_download_result import PreliminaryDownloadResult
from rapidata.api_client.models.private_text_metadata_input import PrivateTextMetadataInput
from rapidata.api_client.models.probabilistic_attach_category_referee_config import ProbabilisticAttachCategoryRefereeConfig
from rapidata.api_client.models.problem_details import ProblemDetails
from rapidata.api_client.models.prompt_metadata import PromptMetadata
from rapidata.api_client.models.prompt_metadata_input import PromptMetadataInput
from rapidata.api_client.models.prompt_metadata_model import PromptMetadataModel
from rapidata.api_client.models.public_order_model import PublicOrderModel
from rapidata.api_client.models.public_text_metadata_input import PublicTextMetadataInput
from rapidata.api_client.models.query_campaigns_model import QueryCampaignsModel
from rapidata.api_client.models.query_model import QueryModel
from rapidata.api_client.models.query_validation_rapids_result import QueryValidationRapidsResult
from rapidata.api_client.models.query_validation_rapids_result_asset import QueryValidationRapidsResultAsset
from rapidata.api_client.models.query_validation_rapids_result_paged_result import QueryValidationRapidsResultPagedResult
from rapidata.api_client.models.query_validation_rapids_result_payload import QueryValidationRapidsResultPayload
from rapidata.api_client.models.query_validation_rapids_result_truth import QueryValidationRapidsResultTruth
from rapidata.api_client.models.query_validation_set_model import QueryValidationSetModel
from rapidata.api_client.models.query_workflows_model import QueryWorkflowsModel
from rapidata.api_client.models.rapid_issue import RapidIssue
from rapidata.api_client.models.rapid_response import RapidResponse
from rapidata.api_client.models.rapid_response_result import RapidResponseResult
from rapidata.api_client.models.rapid_result_model import RapidResultModel
from rapidata.api_client.models.rapid_result_model_result import RapidResultModelResult
from rapidata.api_client.models.rapid_skipped_model import RapidSkippedModel
from rapidata.api_client.models.rapid_state import RapidState
from rapidata.api_client.models.read_bridge_token_keys_result import ReadBridgeTokenKeysResult
from rapidata.api_client.models.register_temporary_customer_model import RegisterTemporaryCustomerModel
from rapidata.api_client.models.register_temporary_customer_result import RegisterTemporaryCustomerResult
from rapidata.api_client.models.report_model import ReportModel
from rapidata.api_client.models.root_filter import RootFilter
from rapidata.api_client.models.scrub_payload import ScrubPayload
from rapidata.api_client.models.scrub_range import ScrubRange
from rapidata.api_client.models.scrub_rapid_blueprint import ScrubRapidBlueprint
from rapidata.api_client.models.scrub_result import ScrubResult
from rapidata.api_client.models.scrub_truth import ScrubTruth
from rapidata.api_client.models.send_completion_mail_step_model import SendCompletionMailStepModel
from rapidata.api_client.models.shape import Shape
from rapidata.api_client.models.simple_workflow_config import SimpleWorkflowConfig
from rapidata.api_client.models.simple_workflow_config_model import SimpleWorkflowConfigModel
from rapidata.api_client.models.simple_workflow_config_model_blueprint import SimpleWorkflowConfigModelBlueprint
from rapidata.api_client.models.simple_workflow_model import SimpleWorkflowModel
from rapidata.api_client.models.simple_workflow_model1 import SimpleWorkflowModel1
from rapidata.api_client.models.simple_workflow_model_blueprint import SimpleWorkflowModelBlueprint
from rapidata.api_client.models.skip_result import SkipResult
from rapidata.api_client.models.sort_criterion import SortCriterion
from rapidata.api_client.models.sort_direction import SortDirection
from rapidata.api_client.models.static_selection import StaticSelection
from rapidata.api_client.models.submit_coco_model import SubmitCocoModel
from rapidata.api_client.models.submit_coco_result import SubmitCocoResult
from rapidata.api_client.models.text_asset import TextAsset
from rapidata.api_client.models.text_asset_model import TextAssetModel
from rapidata.api_client.models.text_asset_model1 import TextAssetModel1
from rapidata.api_client.models.text_asset_model2 import TextAssetModel2
from rapidata.api_client.models.text_metadata import TextMetadata
from rapidata.api_client.models.text_metadata_model import TextMetadataModel
from rapidata.api_client.models.transcription_metadata import TranscriptionMetadata
from rapidata.api_client.models.transcription_metadata_input import TranscriptionMetadataInput
from rapidata.api_client.models.transcription_metadata_model import TranscriptionMetadataModel
from rapidata.api_client.models.transcription_payload import TranscriptionPayload
from rapidata.api_client.models.transcription_rapid_blueprint import TranscriptionRapidBlueprint
from rapidata.api_client.models.transcription_result import TranscriptionResult
from rapidata.api_client.models.transcription_truth import TranscriptionTruth
from rapidata.api_client.models.transcription_word import TranscriptionWord
from rapidata.api_client.models.translated_prompt_metadata_model import TranslatedPromptMetadataModel
from rapidata.api_client.models.translated_string import TranslatedString
from rapidata.api_client.models.unlock_order_result import UnlockOrderResult
from rapidata.api_client.models.update_access_model import UpdateAccessModel
from rapidata.api_client.models.update_campaign_model import UpdateCampaignModel
from rapidata.api_client.models.update_order_model import UpdateOrderModel
from rapidata.api_client.models.update_validation_rapid_model import UpdateValidationRapidModel
from rapidata.api_client.models.update_validation_rapid_model_truth import UpdateValidationRapidModelTruth
from rapidata.api_client.models.upload_coco_result import UploadCocoResult
from rapidata.api_client.models.upload_datapoints_result import UploadDatapointsResult
from rapidata.api_client.models.upload_files_from_s3_bucket_model import UploadFilesFromS3BucketModel
from rapidata.api_client.models.upload_text_sources_to_dataset_model import UploadTextSourcesToDatasetModel
from rapidata.api_client.models.user_score_user_filter_model import UserScoreUserFilterModel
from rapidata.api_client.models.validation_chance import ValidationChance
from rapidata.api_client.models.validation_import_post_request_blueprint import ValidationImportPostRequestBlueprint
from rapidata.api_client.models.validation_selection import ValidationSelection
from rapidata.api_client.models.validation_set_model import ValidationSetModel
from rapidata.api_client.models.validation_set_model_paged_result import ValidationSetModelPagedResult
from rapidata.api_client.models.validation_set_overview_model import ValidationSetOverviewModel
from rapidata.api_client.models.workflow_aggregation_step_model import WorkflowAggregationStepModel
from rapidata.api_client.models.workflow_artifact_model import WorkflowArtifactModel
from rapidata.api_client.models.workflow_config_artifact_model import WorkflowConfigArtifactModel
from rapidata.api_client.models.workflow_config_artifact_model_workflow_config import WorkflowConfigArtifactModelWorkflowConfig
from rapidata.api_client.models.workflow_labeling_step_model import WorkflowLabelingStepModel
from rapidata.api_client.models.workflow_split_model import WorkflowSplitModel
from rapidata.api_client.models.workflow_split_model_filter_configs_inner import WorkflowSplitModelFilterConfigsInner
from rapidata.api_client.models.workflow_state import WorkflowState
