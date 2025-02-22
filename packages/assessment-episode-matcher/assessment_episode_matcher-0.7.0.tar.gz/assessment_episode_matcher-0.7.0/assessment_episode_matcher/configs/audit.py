
# add  issue_type and issue_level to all
additional_fields = ["issue_type"  , "issue_level"]

COLUMNS_AUDIT_DATES = [
  "ESTABLISHMENT IDENTIFIER"
  ,"PMSEpisodeID"
  ,"PMSPersonID"
  ,"SLK"
  ,"RowKey"
  ,"CommencementDate"
  ,"AssessmentDate"
  ,"EndDate"
  ,"Program"
  ,"Staff_x"
  ,"Staff_y"
  ,"SurveyName"
  ,"days_from_start"
  ,"days_from_end"
  ,"min_days"
]

COLUMNS_AUDIT_EPKEY_CLIENT = [ 
"ESTABLISHMENT IDENTIFIER"
  , "PMSEpisodeID"
  , "PMSPersonID"
  , "CommencementDate"
  , "EndDate"
  , "SLK"
  , "Program"
  , "Staff"
]

COLUMNS_AUDIT_EPKEY_CLIENTPROG = [ 
 *COLUMNS_AUDIT_EPKEY_CLIENT, "SLK_Program"
]

COLUMNS_AUDIT_EPKEY_CLIENT = [ *COLUMNS_AUDIT_EPKEY_CLIENT
                            , "closest_atom_SLK"]



COLUMNS_AUDIT_ASMTKEY_CLIENT = [ 
   "SLK"
  , "RowKey"
	, "AssessmentDate"
  , "Program"
	, "Staff"
	, "SurveyName"
]

COLUMNS_AUDIT_ASMTKEY_CLIENTPROG = COLUMNS_AUDIT_ASMTKEY_CLIENT.copy()

COLUMNS_AUDIT_ASMTKEY_CLIENT = [
  *COLUMNS_AUDIT_ASMTKEY_CLIENTPROG 
  , "closest_episode_SLK"]

COLUMNS_AUDIT_DATES.extend(additional_fields)
COLUMNS_AUDIT_EPKEY_CLIENT.extend(additional_fields)
COLUMNS_AUDIT_EPKEY_CLIENTPROG.extend(additional_fields)

COLUMNS_AUDIT_ASMTKEY_CLIENTPROG.extend(additional_fields)
COLUMNS_AUDIT_ASMTKEY_CLIENT.extend(additional_fields)