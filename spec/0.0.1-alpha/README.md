# Container Application Specification

**NOTE**: This is a proof-of-concept effort that is expected to change dramatically.

#### Version 0.0.1-alpha

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The Container Application Specification is licensed under [GNU Free Documentation License Version 1.3, 3 November 2008](https://www.gnu.org/copyleft/fdl.html).

## Introduction

The Container Application specification is a project to describe 'an Application' that is composed of a set of dependent Container Applications (containerapp). The Container Application specification defines a set of files required to describe such a containerapp. These files can then be used by other tools to deploy a containerapp. Developers may use other tools to generate most of the required containerapp files. Additional utilities can also take advantage of the resulting files, such as testing tools.

### Versioning

Within this specification we follow [the semantic versioning pattern](http://semver.org/spec/v2.0.0.html). 

## Revision History

Version | Date | Notes
--- | --- | ---
0.0.1-alpha | 2015-mm-dd | TBD
v1-alpha | 2015-04-10 | reversioned to 0.0.1-alpha


## Specification

### Format

The files describing a containerapp in accordance with the Container Application Specification are represented using [YAML 1.2](http://www.yaml.org/spec/1.2/spec.html) or [JSON](http://json.org/).

All field names in the specification are **case sensitive**.

By convention, the containerapp definition file is named `Nulecule`. The Nulecule is the primary file defining the containerapp and it's relationship to dependencies.

### Data Types

Primitive data types in the Container Application Specification are based on the types supported by the [JSON-Schema Draft 4](http://json-schema.org/latest/json-schema-core.html#anchor8).

The formats defined by the Container Application Specification are:

Common Name | [`type`](#dataTypeType) | [`format`](#dataTypeFormat) | Comments
----------- | ------ | -------- | --------
integer | `integer` | `int32` | signed 64 bits
float | `number` | `float` | 
string | `string` | |
byte | `string` | `byte` |
boolean | `boolean` | |
date | `string` | `date` | As defined by `full-date` - [RFC3339](http://xml2rfc.ietf.org/public/rfc/html/rfc3339.html#anchor14)
dateTime | `string` | `date-time` | As defined by `date-time` - [RFC3339](http://xml2rfc.ietf.org/public/rfc/html/rfc3339.html#anchor14)
password | `string` | `password` | Used to hint UIs the input needs to be obscured.
URL | `URL` | `URL` | As defined by `URL` - [RFC3986 Section 1.1.3](https://tools.ietf.org/html/rfc3986#section-1.1.3)

### Terminology

Container Application

Provider


### Schema

#### <a name="containerAppObject"></a>Container Application Object

This is the root object for the specification.

##### Fields

Field Name | Type | Description
---|:---:|---
<a name="containerAppId"></a>id | `string` | **Required.** The machine readable id of the Container Application.
<a name="containerAppSpecVersion"></a>specversion | `string` | **Required.** The semantic version string of the Container Application Specification used to describe the app. The value MUST be `"0.0.1-alpha"`. 
<a name="containerAppMetadata"></a>metadata | [ [MetadataObject](#metadataObject) ] | **Optional** An object holding optional metadata related to the Container Application, this may include license information or human readable information.
<a name="containerAppGraph"></a>graph | [ [GraphObject](#graphObject) ] | **Required.** A list of depending containerapps. Strings may either match a local sub directory or another containerapp-spec compliant containerapp image that can be pulled via a provider.
<a name="containerAppRequirements"></a>requirements | [ [RequirementsObject](#requirementsObject) ] | **Optional** A list of requirements of this containerapp.


#### <a name="metadataObject"></a>Metadata Object

Metadata for the Container Application.

##### Fields

Field Name | Type | Description
---|:---:|---
<a name="metadataName"></a>name | `string` | **Optional** A human readable name of the containerapp.
<a name="metadataAppVersion"></a>appversion | `string` | **Optional** The semantic version string of the Container Application.
<a name="metadataDescription"></a>description | `string` | **Optional** A human readable description of the Container Application. This may contain information for the deployer of the containerapp.
<a name="metadataLicenseObject"></a>license | [License Object](#licenseObject) | **Optional** The license information for the containerapp.
<a name="metadataKey"></a>arbitrary_data | `string` | **Optional** Arbitrary `key: value` pair(s) of metadata. May contain nested objects.

##### Metadata Object Example:

```yaml
name: myapp
appversion: 1.0.0
description: description of myapp
foo: bar
othermetadata:
  foo: bar
  files: file://path/to/local/file
```

```js
{
  "name": "myapp",
  "appversion": "1.0.0",
  "description": "description of myapp",
  "foo": "bar",
  "othermetadata": {
    "foo": "bar",
    "files": "file://path/to/local/file"
  }
}
```

#### <a name="licenseObject"></a>License Object

License information for the Container Application.

##### Fields

Field Name | Type | Description
---|:---:|---
<a name="licenseName"></a>name | `string` | **Required.** The human readable license name used for the Container Application, no format imposed.
<a name="licenseUrl"></a>url | `string` | **Optional** A URL to the license used for the API. MUST be in the format of a URL.

##### License Object Example:


```yaml
name: Apache 2.0
url: http://www.apache.org/licenses/LICENSE-2.0.html
```
```js
{
  "name": "GNU GPL, Version 3",
  "url": "https://www.gnu.org/copyleft/gpl.html"
}
```


#### <a name="graphObject"></a>Graph Object

The graph is a list of items (containerapps) the Container Application depends on.

##### Fields of a Graph Item Object

Field Name | Type | Description
---|:---:|---
<a name="dependingContainerAppSource"></a>source | `URL` | **Optional** Source location of the Container Application, the source MUST be specified by a valid URL. If source is present, all other fields SHALL be ignored.
<a name="dependingContainerAppParams"></a>params | [ [ParamsObject](#paramsObject) ] | **Optional** A list of [ParamsObject](#paramsObject) that contain provider specific information. If params is present, source field SHALL be ignored.
<a name="dependingContainerAppArtifacts"></a>artifacts | [ [ArtifactsObject](#artifactsObject) ] | **Optional** A list of [ArtifactsObject](#artifactsObject) that contain providr specific information. If artifacts is present, source field SHALL be ignored.

##### Graph Item Object Example:

```yaml
---
atomicapp-zabbix-mongodb:
  source: uri://registry.devops.example.com
  # if no "artifacts" is specified, than it is an external Atomicapp to be pulled 
  # and installed from the specified source
```

```js
{
  "atomicapp-zabbix-mongodb": {
    "source": "uri://registry.devops.example.com"
  }
}
```

#### <a name="paramsObject"></a>Parameters Object

A set of Parameters the containerapp requires, has set some defaults for or needs user input.

##### Fields

Field Name | Type | Description
---|:---:|---
<a name="parametersDescription"></a>description | `string` | **Required.** A human readable description of the parameter.
<a name="parametersConstraints"></a>constraints | [ConstraintObject](#constraintObject) | **Optional** An optional definition of constraints to the parameter.
<a name="parametersDefault"></a>default | `string` | **Optional** An optional default value for the parameter.

##### Parameters Object Example:

```yaml
description: mongoDB Admin password
constraints: 
  - allowed_pattern: "[A-Z0-9]+"
    description: Must consist of characters and numbers only.
```
```js
{
  "description": "mongoDB Admin password",
  "constraints": [
    {
      "allowed_pattern": "[A-Z0-9]+",
      "description": "Must consist of characters and numbers only."
    }
  ]
}
```

#### <a name="constraintObject"></a>Constraint Object

Constraints to the parameter.

##### Fields

Field Name | Type | Description
---|:---:|---
<a name="constraintObjectPattern"></a>allowed_pattern | `string` | **Required.** A regexp declaring the allowed pattern. 
<a name="constraintObjectDescription"></a>description | `string` | **Required.** A human readable description of the parameter.



#### <a name="requirementsObject"></a>Requirements Object

The list of requirements of the Container Application. It may be [Storage Requirement Objects](#storageRequirementsObject) (for a persistent Volume).


#### <a name="storageRequirementsObject"></a>Storage Requirements Object

This describes a requirement for persistent, read-only or read-write storage that should be available to the containerapp on runtime. The name of this object MUST be `"persistentVolume"`.

##### Fields of Storage Requirement

Field Name | Type | Description
---|:---:|---
<a name="containerAppRequirementsName"></a>name | `string` | **Required.** A name associated with the storage requirement.
<a name="containerAppRequirementsAccessMode"></a>accessModes | `string` | **Required.** May be `"ReadWrite"` or `"ReadOnly"`.
<a name="containerAppRequirementsSize"></a>size | `integer` | **Required.** Size of required the storage.

##### Storage Requirement Example:

```yaml
---
- persistentVolume:
    name: "var-lib-mongodb-data"
    accessMode: "ReadWrite"
    size: 4 # GB by default
```
```js
  {
    "persistentVolume": {
      "name": "var-lib-mongodb-data",
      "accessMode": "ReadWrite",
      "size": 4
    }
  }
```


#### <a name="artifactsObject"></a>Artifacts Object

The Artifacts Object describes a list of provider specific artifact items. These artifact items will be used during installation of the containerapp to deploy it to the provider. Each artifact item is a `URL`.

##### Artifacts Example:

```yaml
---
artifacts: # list of files to be processed by the provider selected at install-time
  atomicplatform:
    - file://relative/path/pod.json.tmpl
    - https://git.devops.example.com
  openshift:
    - file://routes.json
    - inherit:
      - atomicplatform
```
```js
{
  "artifacts": {
    "atomicplatform": [
      "file://relative/path/pod.json.tmpl",
      "https://git.devops.example.com"
    ],
    "openshift": [
      "file://routes.json",
      {
        "inherit": [
          "atomicplatform"
        ]
      }
    ]
  }
}
```


## Directory Layout

```
├── Nulecule 
├── Dockerfile
├── <provider_files_dir>
│   ├── ...
│   └── <provider_files>
└── README.md
```

* `Nulecule`: Container Application definition
* `Dockerfile`: standard packaging for this containerapp
* `<provider_files_dir>`: directories of provider-specific files referenced in a containerapp definition file
  * `PROVIDER_FILES`: provider-specific files necessary for deploying to provider
* `README.md`: information for deploying this application


## README.md

The README.md is the human-readable document. It describes the containerapp in enough detail so an operator can make parameterization and other deployment decisions.

NOTE: This is optional. It is possible for some applications to be "self-describing" through well-written descriptions and input validation.


## Conventions

A few conventions are used in the context of Container Applications.

### Parameters for Providers

Each provider in the [ArtifactsObject](#artifactsObject) of the [GraphObject](#graphObject) may correspond to a containerapp level [ParamsObject](#paramsObject). 

