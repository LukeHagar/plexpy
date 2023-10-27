from enum import Enum


class TaskName(Enum):
    BACKUPDATABASE = "BackupDatabase"
    BUILDGRACENOTECOLLECTIONS = "BuildGracenoteCollections"
    CHECKFORUPDATES = "CheckForUpdates"
    CLEANOLDBUNDLES = "CleanOldBundles"
    CLEANOLDCACHEFILES = "CleanOldCacheFiles"
    DEEPMEDIAANALYSIS = "DeepMediaAnalysis"
    GENERATEAUTOTAGS = "GenerateAutoTags"
    GENERATECHAPTERTHUMBS = "GenerateChapterThumbs"
    GENERATEMEDIAINDEXFILES = "GenerateMediaIndexFiles"
    OPTIMIZEDATABASE = "OptimizeDatabase"
    REFRESHLIBRARIES = "RefreshLibraries"
    REFRESHLOCALMEDIA = "RefreshLocalMedia"
    REFRESHPERIODICMETADATA = "RefreshPeriodicMetadata"
    UPGRADEMEDIAANALYSIS = "UpgradeMediaAnalysis"

    def list():
        return list(map(lambda x: x.value, TaskName._member_map_.values()))
