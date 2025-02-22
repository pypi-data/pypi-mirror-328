_B='(Valide seulement si la première ligne est les en-têtes)'
_A=None
from pydantic import BaseModel,Field,model_validator
from enum import Enum
class ReaderCsvCurveParserNameConfig(str,Enum):COL_X='col_x';COLS_COUPLE='cols_couple'
class ReaderCsvCurveParserColXConfig(BaseModel):x:int|str|list[str]=Field(default=1,description="Si `integer`, index de la colonne pour l'axe x (index `1` pour la première colonne)."+"Si `String`, nom de la colonne pour l'axe x. Si la colonne n'existe pas, il n'y aura pas de parsing."+_B+"Si `List[String] (utiles dans un contexte multi dataset), noms de la colonne pour l'axe x, noms des colonnes pour l'axe x , si plusieurs colonnes correspondent, la première trouvée sera utilisée. Si aucune colonne ne correspond, il n'y aura pas de parsing."+_B)
class ReaderCsvCurveParserColsCoupleConfig(BaseModel):x_index:int=Field(description='NOT IMPLEMENTED - Index Col x');y_index:int=Field(description='NOT IMPLEMENTED - Index Col y')
class ReaderCsvCurveParserConfig(BaseModel):
	name:ReaderCsvCurveParserNameConfig=Field(description='Le type de `paramètres` dépend de cette valeur');parameters:ReaderCsvCurveParserColXConfig|ReaderCsvCurveParserColsCoupleConfig=Field(description='Paramètres du parser de courbes')
	@model_validator(mode='after')
	def validate_model(cls,model):
		A=model
		if isinstance(A.parameters,ReaderCsvCurveParserColXConfig)and A.name!=ReaderCsvCurveParserNameConfig.COL_X or isinstance(A.parameters,ReaderCsvCurveParserColsCoupleConfig)and A.name!=ReaderCsvCurveParserNameConfig.COLS_COUPLE:raise ValueError(f"Curve Parser {A.name} Parameters are not correct")
		if isinstance(A.parameters,dict):
			if A.name==ReaderCsvCurveParserNameConfig.COL_X:A.parameters=ReaderCsvCurveParserColXConfig(**A.parameters)
			elif A.name==ReaderCsvCurveParserNameConfig.COLS_COUPLE:A.parameters=ReaderCsvCurveParserColsCoupleConfig(**A.parameters)
		return A
class ReaderCsvConfig(BaseModel):ignore_colunmns:list[str]|_A=Field(default=_A,description='Liste des noms des colonnes à ignorer. (Valide seulement si la première ligne est les en-têtes)');curve_parser:ReaderCsvCurveParserConfig|_A=Field(default=_A,description='Parseur de courbe à utiliser.')