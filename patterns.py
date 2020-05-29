DB_Patterns=r"    patterns = (dapi[A-Za-z0-9]|dapi)[A-Za-z0-9]{32}"
SQL_Patterns=r"    patterns = (\"|')?(SQL|sql|Sql)?_?(ADMIN|admin|Admin)?_?(CREDENTIAL|credential|Credential)?_?(PWD|pwd|Pwd)?_?(PASSWORD|password|Password)(\"|')?\\s*(:|=>|=)\\s*(\"|')?\\s*.+{10,15}(\"|')?"
Storage_Blob_Patterns=r"    patterns = (\"|')?(STORAGE|storage|Storage)?_?(ACCOUNT|account|Account)?_?(ACCESS|access|Access)?_?(KEY|key|Key)(\"|')?\\s*(:|=>|=)\\s*(\"|')?[A-zA-Za-z0-9+/=!@$%&*?"#"\\^+=]{88}(\"|')?
GIT_Pat_Patterns=r"    patterns = (\"|')?(GIT|git|Git)?_?(PAT|pat|Pat)?_?(TOKEN|token|Token)?_?(SECRET|secret|Secret)(\"|')?\\s*(:|=>|=)\\s*(\"|')?[A-zA-Za-z0-9!@$%&*?"#"\\^+=]{40}(\"|')?
SQL_Pwd_patterns=r"    patterns = (\"|')?(SQL|sql|Sql)?_?(ADMIN|admin|Admin)?_?(CREDENTIAL|credential|Credential)?_?(PWD|pwd|Pwd)(\"|')?\\s*(:|=>|=)\\s*(\"|')?[A-zA-Za-z0-9!@$%&*?"#"\\^=]{10,15}(\"|')?

path = 'D:/a/1/s/.git/config'

with open(path, "a") as myfile:
    myfile.write('\n'+DB_Patterns+'\n'+SQL_Patterns+'\n'+Storage_Blob_Patterns+'\n'+GIT_Pat_Patterns+'\n'+SQL_Pwd_patterns)
