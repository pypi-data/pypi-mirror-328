### BioTuring SpatialX Connector

#### Installation

```python
!pip install -U spatialx_connector
```


#### Import


```python
import warnings
warnings.filterwarnings("ignore")
```


```python
import os

import spatialx_connector

from spatialx_connector import SpatialXConnector
from spatialx_connector import Technologies
from spatialx_connector import DefaultGroup
from spatialx_connector import Species

from spatialx_connector import ConnectorKeys
from spatialx_connector import SubmissionElementKeys
from spatialx_connector import ExtendSegmentationSubmission
from spatialx_connector import ExtendExpressionSubmission
```

#### Domain and Token


```python
DOMAIN = "DOMAIN"
TOKEN = "TOKEN"
```

#### Explore Account

##### Information


```python
connector = SpatialXConnector(domain=DOMAIN, token=TOKEN)
spatialx_connector.format_print(connector.info)
```


```python
spatialx_connector.format_print(connector.groups)
```

##### Storage


```python
spatialx_connector.format_print(connector.s3)
```


```python
spatialx_connector.format_print(connector.folders)
```

##### Study Information


```python
studies = connector.list_study(
    group=DefaultGroup.PERSONAL_WORKSPACE.value,
    species=Species.HUMAN.value,
)
spatialx_connector.format_print(studies)
```


```python
study_details = connector.get_study_detail(studies[0][ConnectorKeys.STUDY_ID.value])
spatialx_connector.format_print(study_details)
```

##### Sample Information


```python
samples = connector.list_sample(studies[0][ConnectorKeys.STUDY_ID.value])
spatialx_connector.format_print(samples)
```


```python
sample_details = connector.get_sample_detail(samples[0][ConnectorKeys.SAMPLE_ID.value])
spatialx_connector.format_print(sample_details)
```

#### Uploading


```python
uploading_results = connector.upload_file("/s3/colab/content/xenium/experiment.xenium")
spatialx_connector.format_print(uploading_results)
```


```python
uploading_results = connector.upload_big_file("/s3/colab/content/xenium/morphology_mip.ome.tif", debug_mode=True)
spatialx_connector.format_print(uploading_results)
```


```python
uploading_results = connector.upload_folder("/s3/colab/content/xenium", debug_mode=True)
spatialx_connector.format_print(uploading_results)
```

#### Submission

##### Submit data


```python
visium_submission_information = connector.parse_data_information(
    "Visium_V2_Human_Colon_Cancer_P2",
    Technologies.VISIUM.value,
    os.path.join(
        connector.s3["bioturingpublic"],
        "SpatialX_datasets/Human_Colon_Cancer_P2/Visium_V2_Human_Colon_Cancer_P2"
    )
)
spatialx_connector.format_print(visium_submission_information)
```


```python
xenium_submission_information = connector.parse_data_information(
    "Xenium_V1_Human_Colon_Cancer_P2_CRC_Add_on_FFPE",
    Technologies.XENIUM.value,
    os.path.join(
        connector.s3["bioturingpublic"],
        "SpatialX_datasets/Human_Colon_Cancer_P2/Xenium_V1_Human_Colon_Cancer_P2_CRC_Add_on_FFPE"
    )
)
spatialx_connector.format_print(xenium_submission_information)
```


```python
submission_results = connector.submit(
    DefaultGroup.PERSONAL_WORKSPACE.value,
    Species.HUMAN.value,
    "10xgenomics",
    "Human_Colon_Cancer_P2",
    visium_submission_information
)
spatialx_connector.format_print(submission_results)
```


```python
xenium_submission_results = connector.add_sample_data(
    submission_results[ConnectorKeys.STUDY_ID.value],
    submission_results[ConnectorKeys.SAMPLE_ID.value],
    xenium_submission_information,
)
submission_results[ConnectorKeys.SAMPLE_DATA.value].extend(xenium_submission_results[ConnectorKeys.SAMPLE_DATA.value])
spatialx_connector.format_print(submission_results)
```

##### Submit multiple samples


```python
multiple_samples_submission_information = connector.parse_multiple_samples_information(
    Technologies.COSMX_VER1.value,
    os.path.join(
        connector.s3["bioturingpublic"],
        "SpatialX_datasets/COSMX_VER1"
    )
)
spatialx_connector.format_print(multiple_samples_submission_information)
```


```python
multiple_samples_submission_results = connector.submit_multiple_samples(
    DefaultGroup.PERSONAL_WORKSPACE.value,
    Species.HUMAN.value,
    "Multiple CosMX Ver1",
    multiple_samples_submission_information
)
spatialx_connector.format_print(multiple_samples_submission_results)
```

##### Add extend elements


```python
DATA_ID = "DATA ID"
```


```python
sample_data_info = connector.get_sample_data_detail(DATA_ID)
spatialx_connector.format_print(sample_data_info)
```


```python
add_segmentation_result = connector.add_sample_data_element(
    title="Proteomics Segmentation",
    study_id=sample_data_info[ConnectorKeys.STUDY_ID.value],
    sample_id=sample_data_info[ConnectorKeys.SAMPLE_ID.value],
    data_id=sample_data_info[ConnectorKeys.DATA_ID.value],
    adding_types=[ExtendSegmentationSubmission.PARQUET.value],
    paths={
        SubmissionElementKeys.SEGMENTATION.value: os.path.join(
            connector.s3["bioturingpublic"],
            "SpatialX_datasets/human_pancreas_codex/human_pancreas_segmentation.parquet",
        )
    }
)
spatialx_connector.format_print(add_segmentation_result)
```


```python
sample_data_elements = connector.get_sample_data_elements(DATA_ID)
spatialx_connector.format_print(sample_data_elements)
```


```python
add_expression_result = connector.add_sample_data_element(
    title="Proteomics Expression",
    study_id=sample_data_info[ConnectorKeys.STUDY_ID.value],
    sample_id=sample_data_info[ConnectorKeys.SAMPLE_ID.value],
    data_id=sample_data_info[ConnectorKeys.DATA_ID.value],
    adding_types=[ExtendExpressionSubmission.IMPORT_ANNDATA.value],
    paths={
        SubmissionElementKeys.EXPRESSION.value: os.path.join(
            connector.s3["bioturingpublic"],
            "SpatialX_datasets/human_pancreas_codex/human_pancreas_protein.h5ad",
        ),
    },
    args={
        SubmissionElementKeys.SPATIAL_ID.value: sample_data_elements[SubmissionElementKeys.CELL_CENTERS.value][0],
    }
)
spatialx_connector.format_print(add_expression_result)
```


#### Analysis


```python
data_id = submission_results["sample_data"][-1]["data_id"]
data_id
```


##### Embeddings


```python
response = connector.analysis.embeddings.pca(data_id=data_id, title="Connector - PCA")
spatialx_connector.format_print(response)
```



```python
response = connector.analysis.embeddings.scvi(data_id=data_id, title="Connector - scVI", n_top_genes=2000)
spatialx_connector.format_print(response)
```


```python
embeddings = connector.analysis.list_embedding(data_id)
spatialx_connector.format_print(embeddings)
```


```python
response = connector.analysis.embeddings.umap(data_id=data_id, embedding_key=embeddings[0], title="Connector - UMAP")
spatialx_connector.format_print(response)
```


```python
response = connector.analysis.embeddings.tsne(data_id=data_id, embedding_key=embeddings[0], title="Connector - tSNE")
spatialx_connector.format_print(response)
```


##### Clustering


```python
response = connector.analysis.clustering.louvain(
    data_id=data_id,
    embedding_key=embeddings[0],
    resolution=0.1,
    title="Connector - Louvain",
)
spatialx_connector.format_print(response)
```


```python
response = connector.analysis.clustering.kmeans(
    data_id=data_id,
    embedding_key=embeddings[0],
    n_clusters=5,
    title="Connector - k-means",
)
spatialx_connector.format_print(response)
```


##### Prediction


```python
embeddings = connector.analysis.list_embedding(data_id)
spatialx_connector.format_print(embeddings)
```


```python
metadata = connector.analysis.list_metadata(data_id)
spatialx_connector.format_print(metadata)
```


```python
response = connector.analysis.prediction.metadata_reference(
    data_id=data_id,
    cluster_key=metadata[0],
    species=spatialx_connector.Species.HUMAN.value.value,
    title="Connector - Metadata Reference",
)
spatialx_connector.format_print(response)
```


##### Differential Expression


```python
response = connector.analysis.de.differential_expression_genes(
    data_id_1=data_id,
    data_id_2=data_id,
    group_1_indices=[i for i in range(10000)],
    group_2_indices=[i for i in range(10000, 20000)],
    title="Connector - DE genes",
)
spatialx_connector.format_print(response)
```


##### Spatial Analysis


```python
response = connector.analysis.spatial_analysis.region_segmentation(
    data_id=data_id,
    radius=50,
    mpp=0.2125,
    resolution=0.5,
    species=spatialx_connector.Species.HUMAN.value.value,
    title="Connector - Region Segmentation",
)
spatialx_connector.format_print(response)
```


#### Convert data from Lens


```python
!pip install bioturing_connector
```


```python
LENS_SC_HOST: str = "LENS_SC_HOST"
LENS_SC_TOKEN: str = "LENS_SC_TOKEN"
lens_sc_studies = connector.list_lens_sc_studies(
    host=LENS_SC_HOST, token=LENS_SC_TOKEN,
    group=spatialx_connector.DefaultGroup.PERSONAL_WORKSPACE,
    species=spatialx_connector.Species.HUMAN.value.value,
)
spatialx_connector.format_print(lens_sc_studies)
```


```python
# Convert a study
connector.convert_data_from_lens(lens_sc_studies[0])
```


```python
LENS_BULK_HOST: str = "LENS_BULK_HOST"
LENS_BULK_TOKEN: str = "LENS_BULK_TOKEN"
lens_bulk_studies = connector.list_lens_bulk_studies(
    host=LENS_BULK_HOST, token=LENS_BULK_TOKEN,
    group=spatialx_connector.DefaultGroup.PERSONAL_WORKSPACE,
    species=spatialx_connector.Species.HUMAN.value.value,
)
spatialx_connector.format_print(lens_bulk_studies)
```


```python
# Convert multiple studies
connector.convert_data_from_lens(lens_bulk_studies)
```
