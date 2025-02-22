import json
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional, Union


@dataclass
class Message():
    role: str
    content: str

    @staticmethod
    def from_dict(obj: Dict[str, Any]):
        role = obj['role']
        content = obj['content']
        return Message(role=role, content=content)


@dataclass
class Prompt:
    prompt_id: str
    version: int
    version_id: str
    messages: List[Message]
    model_parameters: Dict[str, Union[str, int, bool, Dict, None]]
    model: Optional[str] = None
    tags: Optional[Dict[str, Union[str, int, bool, None]]] = None

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Prompt":
        return Prompt(
            prompt_id=data['promptId'],
            version=data['version'],
            version_id=data['versionId'],
            messages=[Message.from_dict(m) for m in data['messages']],
            model_parameters=data['modelParameters'],
            model=data['model'],
            tags=data['tags']
        )


@dataclass
class RuleType():
    field: str
    value: Union[str, int, List[str], bool, None]  # adding None here
    operator: str
    valueSource: Optional[str] = None
    exactMatch: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Dict):
        return RuleType(field=obj['field'], value=obj['value'], operator=obj['operator'], valueSource=obj.get('valueSource', None), exactMatch=obj.get('exactMatch', None))


@dataclass
class RuleGroupType():
    rules: List[Union['RuleType', 'RuleGroupType']]
    combinator: str

    @staticmethod
    def from_dict(obj: Dict):
        rules = []
        for rule in obj['rules']:
            if 'rules' in rule:
                rules.append(RuleGroupType.from_dict(rule))
            else:
                rules.append(RuleType(**rule))
        return RuleGroupType(rules=rules, combinator=obj['combinator'])


@dataclass
class PromptDeploymentRules():
    version: int
    query: Optional[RuleGroupType] = None

    @staticmethod
    def from_dict(obj: Dict):
        query = obj.get('query', None)
        if query is not None:
            query = RuleGroupType.from_dict(query)
        return PromptDeploymentRules(version=obj['version'], query=query)


@dataclass
class VersionSpecificDeploymentConfig():
    id: str
    timestamp: datetime
    rules: PromptDeploymentRules
    isFallback: bool = False

    @staticmethod
    def from_dict(obj: Dict):
        rules = PromptDeploymentRules.from_dict(obj['rules'])
        return VersionSpecificDeploymentConfig(id=obj['id'], timestamp=obj['timestamp'], rules=rules, isFallback=obj.get('isFallback', False))


@dataclass
class PromptVersionConfig():
    messages: List[Message]
    modelParameters: Dict[str, Union[str, int, bool, Dict, None]]
    model: str
    tags: Optional[Dict[str, Union[str, int, bool, None]]] = None

    @staticmethod
    def from_dict(obj: Dict):
        messages = [Message.from_dict(message) for message in obj['messages']]
        return PromptVersionConfig(messages=messages, modelParameters=obj['modelParameters'], model=obj['model'], tags=obj.get('tags', None))


@dataclass
class PromptVersion():
    id: str
    version: int
    promptId: str
    createdAt: str
    updatedAt: str
    deletedAt: Optional[str] = None
    description: Optional[str] = None
    config: Optional[PromptVersionConfig] = None

    @staticmethod
    def from_dict(obj: Dict):
        config = obj.get('config', None)
        if config:
            config = PromptVersionConfig.from_dict(config)
        return PromptVersion(id=obj['id'], version=obj['version'], promptId=obj['promptId'], createdAt=obj['createdAt'], updatedAt=obj['updatedAt'], deletedAt=obj.get('deletedAt', None), description=obj.get('description', None), config=config)


@dataclass
class VersionsAndRules():
    rules: Dict[str, List[VersionSpecificDeploymentConfig]]
    versions: List[PromptVersion]
    folderId: Optional[str] = None
    fallbackVersion: Optional[PromptVersion] = None

    @staticmethod
    def from_dict(obj: Dict):
        rules = obj['rules']
        # Decoding each rule
        for key in rules:
            rules[key] = [VersionSpecificDeploymentConfig.from_dict(
                rule) for rule in rules[key]]
        versions = [PromptVersion.from_dict(version)
                    for version in obj['versions']]
        fallbackVersion = obj.get('fallbackVersion', None)
        if fallbackVersion:
            fallbackVersion = PromptVersion.from_dict(fallbackVersion)
        return VersionsAndRules(rules=rules, versions=versions,  folderId=obj.get('folderId', None), fallbackVersion=fallbackVersion)

    def to_json(self):
        return asdict(self)


@ dataclass
class VersionAndRulesWithPromptId(VersionsAndRules):
    promptId: str = ""

    @ staticmethod
    def from_dict(obj: Dict):
        promptId = obj['promptId']
        del obj['promptId']
        versionAndRules = VersionsAndRules.from_dict(obj)
        return VersionAndRulesWithPromptId(rules=versionAndRules.rules, versions=versionAndRules.versions, promptId=promptId, folderId=versionAndRules.folderId, fallbackVersion=versionAndRules.fallbackVersion)


class VersionAndRulesWithPromptIdEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, VersionAndRulesWithPromptId):
            return asdict(o)
        return super().default(o)


@ dataclass
class Error():
    message: str


@ dataclass
class PromptData():
    promptId: str
    rules: Dict[str, List[VersionSpecificDeploymentConfig]]
    versions: List[PromptVersion]
    folderId: Optional[str] = None
    fallbackVersion: Optional[PromptVersion] = None


@ dataclass
class MaximApiPromptResponse():
    data: VersionsAndRules
    error: Optional[Error] = None


@ dataclass
class MaximApiPromptsResponse():
    data: List[PromptData]
    error: Optional[Error] = None


@ dataclass
class MaximAPIResponse():
    error: Optional[Error] = None
