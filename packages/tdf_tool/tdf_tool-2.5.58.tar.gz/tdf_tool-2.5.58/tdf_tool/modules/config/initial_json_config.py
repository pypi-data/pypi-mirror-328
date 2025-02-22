import json
import os
import subprocess
from ruamel import yaml
from typing import Tuple
from tdf_tool.tools.print import Print
from tdf_tool.tools.shell_dir import ShellDir


class InitialJsonConfig:
    
    def __init__(self):
        config = self.__getInitialConfig()
        self.featureBranch = config[0]
        self.shellName = config[1]
        self.moduleNameList = config[2]
        
    # 获取当前分支
    def get_current_branch(self):
        result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True)
        return result.stdout.strip()
    
    def get_project_name(self):
        with open("pubspec.yaml", encoding="utf-8") as f:
            doc = yaml.round_trip_load(f)
            node = "name"
            if isinstance(doc, dict) and doc.__contains__(node) and isinstance(doc[node], str):
                return doc[node]
        return None
        
    # 获取环境配置文件
    def __getInitialConfig(self) -> Tuple:
        ShellDir.goInShellDir()
        if os.path.exists("tdf_cache") is not True:
            Print.error("读取项目环境配置文件initial_config.json失败")
        currentPath = os.getcwd()
        
        currentFeatureBranch = self.get_current_branch()
        shellName = self.get_project_name()
        

        jsonData = dict
        with open("./tdf_cache/initial_config.json", "r", encoding="utf-8") as rf:
            jsonData = json.loads(rf.read())
            rf.close()
            if (
                isinstance(jsonData, dict)
                and jsonData.__contains__("moduleNameList")
            ):    
                self.__initialDepsEnhancement(jsonData)
                return (
                    currentFeatureBranch,
                    shellName,
                    jsonData["moduleNameList"],
                )
            else:
                Print.error("读取项目环境配置文件initial_config.json失败")
    
    def __initialDepsEnhancement(self, jsonData: dict):
        self.forceOverrides: list = []
        if (jsonData.__contains__("depsEnhancement")):
            innerJson = jsonData["depsEnhancement"]
            if isinstance(innerJson, dict) and innerJson.__contains__("forceOverrides"):
                overrideJson = innerJson["forceOverrides"]
                if isinstance(overrideJson, dict):
                    print(overrideJson)
                    self.forceOverrides = [{item: overrideJson[item]} for item in overrideJson]
                    
           