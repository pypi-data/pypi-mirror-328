#!/usr/bin/python3 -u

from git import Repo
from py_console import console
import confuse
import hcl
import os
import sys

class Core():
    def __init__(self, action, target_environment=None):
        self.app_name = os.path.basename(sys.argv[0])
        self.app_config = os.path.basename(os.path.dirname(__file__))
        self.action = action
        if self.action != "help":
            self.get_platform()
            self.build_id = os.getenv('BUILD_ID')
            self.target_environment = target_environment
            self.location = os.path.realpath(os.getcwd())
            self.repo_name = str(os.path.splitext(os.path.basename(self.repo_url))[0]).lower()
            self.branch_name = str(Repo(self.repo_root).active_branch).lower()
            self.clouds_list = ['aws', 'azr', 'vmw', 'gcp']
            self.global_resources = ["53", "global"]
            self.get_default_variables()
            self.options_dict = {
                "bucket_prefix": "inf.tfstate", 
                "tf_cloud_org": None
                }
            self.bucket_prefix = self.set_config_var('bucket_prefix')
            self.tf_cloud_org1 =  self.set_config_var('tf_cloud_org')
            self.user_config_path = self.load_configs()[1]
            self.resource = os.path.relpath(self.location, self.repo_root).replace('\\', '/')
            self.config_files = self.load_configs()
            self.secret_path = os.path.join("{}".format(self.repo_root), "secret_{}_backend.tfvars".format(self.cloud))
            self.get_env_files()
            self.get_deployment_attributes()
            self.sanity_check()
            self.set_site_configuration()
            self.set_backend_configuration(self.backend.lower())
            self.export_environment()

    def get_platform(self):
        try:
            repo_root = Repo(search_parent_directories=True).git.rev_parse("--show-toplevel")
        except:
            console.error("  You are not executing " + self.app_config.upper() + " from a git repository !\n  Please ensure execution from a resurce directory inside a git repository !\n", showTime=False)
            sys.exit(2)

        if sys.platform.startswith("win"):
            self.platform = "windows"
            self.repo_root = repo_root.replace('/', '\\')
        else:
            self.platform = "linux"
            self.repo_root = repo_root

        try:
            self.repo_url = Repo(self.repo_root).remotes[0].config_reader.get("url")
        except IndexError:
            console.error("  " + str(os.path.splitext(os.path.basename(self.repo_root))[0]).upper() + " is a local repository with no remotes. !\n", showTime=False)
            sys.exit(2)

    def load_configs(self):
        config = confuse.LazyConfig(self.app_config, __name__)
        user_config_path = config.user_config_path()
        if os.path.isfile(user_config_path):
            config.set_file(user_config_path, base_for_paths=True)
        return config, user_config_path

    def set_config_var(self, var):
        if os.environ.get(var.upper()) is not None:
            env_var = os.environ[var.upper()]
        else:
            env_var = self.load_configs()[0][var].get(confuse.Optional(str, default=self.options_dict[var]))
        return env_var


    def get_default_variables(self):
        """
        Get Repository Prefix, Cloud Dependent Project, Account, Environment variables.
        """

        self.repo_name_parts = self.repo_name.split("-")

        if len(self.repo_name_parts) > 2:
            self.repo_prefix = "-".join(self.repo_name_parts[:-2])
        else:
            self.repo_prefix = ""

        if len(self.repo_name_parts) <= 1:
            console.error(
                "Error: Invalid repository name structure.\n"
                "The repository name structure needs to be:\n"
                "  [Repository Prefix]-[Hosting Platform]-[Project name]\n"
                "  Note: Project Prefix is optional.\n"
                "  Example:\n"
                "    - myrepo-aws-myproject\n"
                "    - aws-myproject\n"
                "Default supported Hosting Platform values are:\n  " + ", ".join(self.clouds_list) + "\n",
                showTime=False
            )
            sys.exit(2)
        else:
            self.cloud = self.repo_name_parts[-2]

        if self.cloud in self.clouds_list:
            self.project = self.repo_name_parts[-1]
            self.account = self.branch_name.split("-")[0]
            if len(self.branch_name.split("-")) == 2: 
                self.environment = self.branch_name.split("-")[1]
            else:
                console.error("  Error: Invalid repository branch name structure.\n"
                              "  For Cloud Hosting Platforms, he branch name structure needs to be:\n"
                              "  [Account Number]-[Environment Name]\n"
                              "  Example:\n    - 31234565435-uat\n", showTime=False)
                sys.exit(2)
        else:
            self.project = self.repo_name.split("-")[-1]
            if len(self.branch_name.split("-")) == 2:
                self.account = self.branch_name.split("-")[0]
                self.environment = self.branch_name.split("-")[1]
            else:
                self.account = 'none'
                self.environment = self.branch_name

    def get_env_files(self):
        """
        Return Appropriate Env File Based on whether there is
        a target deployment defined in the init attributes.
        """
        if self.target_environment:
            file_preffix = "{}_{}".format(self.environment, self.target_environment)
        else:
            file_preffix = "{}".format(self.environment)
        
        self.common_shell_file = os.path.join(
            self.repo_root, "common", "environments","env_{}.hcl".format(file_preffix))
        self.common_env_file = os.path.join(
            self.repo_root, "common", "environments","env_{}_common.tfvars".format(file_preffix))
        self.local_env_file = os.path.join(
            self.location, "environments", "env_{}.tfvars".format(file_preffix))

    def get_deployment_attributes(self):
        """
        Extract deployment attributes from shell env file.
        This is done to maintain backward compatibility with
        current deployments, but should be migrated to a declarative
        language in the future, ie: json,yaml.
        """

        if not os.path.isfile(self.common_shell_file):
            console.error("  No Common Wrapper Shell File available ! Please create:\n  " + self.common_shell_file + "\n  and add configuration content if necessary !\n", showTime=False)
            sys.exit(2)

        try:    
            with open(self.common_shell_file, 'r') as fp:
                obj = hcl.load(fp)
                self.china_deployment = obj.get('china_deployment', '').lower()
                self.dr = obj.get('dr', '').lower()
                self.global_resource = obj.get('global_resource', '').lower()
                self.target_environment_type = obj.get('target_environment_type', 'region').lower()
                self.mode = obj.get('mode', '').lower()
                self.region = obj.get('region', '').lower()
                self.backend = obj.get('backend', '').lower()
                self.tf_cloud_backend = obj.get('tf_cloud_backend', 'simple')   .lower()            
                self.tf_cloud_org2 = obj.get('tf_cloud_org', '').lower()               
                if sys.platform.startswith("win"):
                    self.tf_cli_args = obj.get('tf_cli_args', '').replace('"','').replace('${REPO_PATH}',self.repo_root).replace('$REPO_PATH',self.repo_root).replace('\\', '\\\\').replace('/', '\\\\')
                else:
                    self.tf_cli_args = obj.get('tf_cli_args', '').replace('"','').replace('${REPO_PATH}',self.repo_root).replace('$REPO_PATH',self.repo_root)
        except KeyError:
            console.error("  Missing Common Shell Env File: \n          {}\n".format(self.common_shell_file), showTime=False)
            sys.exit(2)
        except(ValueError):
            pass   

    def sanity_check(self):
        """
        Series of sanity Checks performed to ensure what we
        are working with.
        """

        self.var_file_args_list = []
        self.var_file_args = ''

        if os.path.isfile(self.secret_path):
            self.var_file_args_list.append(self.secret_path)

        if self.location == self.repo_root:
            console.error("  You are executing " + self.app_name.upper() + " from the repository root !\n          Please ensure execution from a resurce directory !\n", showTime=False)
            sys.exit(2)

        if not os.path.isfile(self.local_env_file):
            console.error("  No Local Environment Files at this location !\n", showTime=False)
            if not any(File.endswith(".tf") for File in os.listdir(self.location)):
                console.error("  You are executing " + self.app_name.upper() + " from an improper location,\n          Please ensure execution from a resurce directory !\n", showTime=False)
                sys.exit(2)
            else:
                console.error("  Please create:\n          " + self.local_env_file + "\n          and add configuration content if necessary !\n", showTime=False)
                sys.exit(2)
        else:
            self.var_file_args_list.append(self.local_env_file)

        if not os.path.isfile(self.common_env_file):
            console.success("  No Common Environment File available ! Please create:\n            " + self.common_env_file + "\n            and add configuration content if necessary !\n", showTime=False)
            #sys.exit(2)
        else:
            self.var_file_args_list.append(self.common_env_file)

        if not self.region:
            if self.cloud in ['aws', 'azr']:
                console.error("  Specify 'region' in the file: \n          " + self.common_shell_file, showTime=False)
                sys.exit(2)
        
        if self.target_environment_type not in ["region", "site"]:
            console.error("  Specify a valid Target Environment Type (region/site) in the file: \n  " + self.common_shell_file, showTime=False)
            sys.exit(2)

        arg_prefix = '-var-file='
        self.var_file_args = [arg_prefix + item for item in self.var_file_args_list]

    def set_site_configuration(self):
        """
        Parse Data returned by get_deployment_attributes and
        return prefix and module for blue/green, site or
        the default region based deployment.
        """

        if self.target_environment and self.target_environment_type != 'region':
            self.site = self.target_environment
            if self.mode != '':
                self.prefix = "{}-{}-{}".format(self.project, self.target_environment, self.mode)
                self.module = "{}-{}".format(self.resource, self.mode)
            else:
                self.prefix = "{}-{}".format(self.project, self.target_environment)
                self.module = self.resource
        else:
            self.site = ''
            if self.mode != '':
                self.prefix = "{}-{}".format(self.project, self.mode)
                self.module = "{}-{}".format(self.resource, self.mode)
            else:
                self.prefix = self.project
                self.module = self.resource

    def set_backend_configuration(self, backend_type=None):
        """
        Parse Data returned by get_deployment_attributes and
        return bucket, backend_region for deployment.
        """

        self.backend_type = backend_type or self.cloud
        self.backend_region = None
        self.tf_cloud_backend_org = None
     
        if self.backend_type == "aws":
            if self.global_resource == "true" or any(word in self.resource for word in self.global_resources):
                self.bucket_key = "{prefix}/{module}/terraform.tfstate".format(
                    prefix=self.prefix,
                    module=self.module
                )            
            else:
                self.bucket_key = "{prefix}/{region}/{module}/terraform.tfstate".format(
                    prefix=self.prefix,
                    region=self.region,
                    module=self.module
                )

            if self.dr == "true":
                self.bucket = "{}.{}.{}.dr".format(self.bucket_prefix, self.account, self.environment)
                if self.china_deployment == "true":
                    self.backend_region = "cn-northwest-1"
                else:
                    self.backend_region = "us-west-2"
            else:   
                self.bucket = "{}.{}.{}".format(self.bucket_prefix, self.account, self.environment)
                if self.china_deployment == "true":
                    self.backend_region = "cn-north-1"
                else:
                    self.backend_region = "us-east-1"
        elif self.backend_type == "azr":
            if self.global_resource == "true" or any(word in self.resource for word in self.global_resources):    
                self.bucket_key = "{env}/{prefix}/{module}/terraform.tfstate".format(
                    env=self.environment,
                    region=self.region,
                    module=self.module
                )
            else:
                self.bucket_key = "{env}/{prefix}/{region}/{module}/terraform.tfstate".format(
                    env=self.environment,
                    prefix=self.prefix,
                    region=self.region,
                    module=self.module
                )

            self.bucket_prefix = ''.join(char.lower() for char in self.bucket_prefix if char.isalnum())
            if self.dr == "true":
                self.bucket = "{}{}{}dr".format(self.bucket_prefix, self.account, self.environment)
            else:
                self.bucket = "{}{}{}".format(self.bucket_prefix, self.account, self.environment)
            
            if len(self.bucket) > 24:
                console.error("  Storage Account Name exceeds 24 characters.\n  Storage Account: " + self.bucket + "\n  Please provide a shorter name.\n", showTime=False)
                sys.exit(2)

        elif self.backend_type == "tfc" or self.tf_cloud_backend == "true":
            if self.tf_cloud_backend == "simple":
                self.bucket_key = "{env}-{prefix}-{module}".format(
                    env=self.environment,
                    prefix=self.prefix.replace("/","-"),
                    module=self.module.replace("/","-")
                )
            elif self.tf_cloud_backend == "extended":
                if self.global_resource == "true" or any(word in self.resource for word in self.global_resources):
                    self.bucket_key = "{cloud}-{env}-{prefix}-{module}".format(
                        cloud = self.cloud,
                        env=self.environment,
                        prefix=self.prefix.replace("/","-"),
                        module=self.module.replace("/","-")
                    )
                else:
                    self.bucket_key = "{cloud}-{env}-{prefix}-{region}-{module}".format(
                        cloud = self.cloud,
                        env=self.environment,
                        prefix=self.prefix.replace("/","-"),
                        region=self.region.replace("-",""),
                        module=self.module.replace("/","-")
                    )
            else:
                console.error("  Invalid tf_cloud_backend value.\n  Please provide a valid value: simple/extended\n", showTime=False)
                sys.exit(2)
            if self.tf_cloud_org1:
                self.tf_cloud_backend_org = self.tf_cloud_org1
            else:
                self.tf_cloud_backend_org = self.tf_cloud_org2
            self.backend_region = "none"
            self.bucket = "none"
        else:
            self.bucket_key = "none"
            self.backend_region = "none"
            self.bucket = "none"

    def export_environment(self):
        """
        Export the environemt Variables to be used by
        Terraform.
        """
        
        self.my_env = dict(os.environ, 
            **{"TF_VAR_deployment_region": self.region},
            **{"TF_VAR_backend_region": self.backend_region},
            **{"TF_VAR_project": self.project},
            **{"TF_VAR_account": self.account},
            **{"TF_VAR_mode": self.mode},
            **{"TF_VAR_env": self.environment},
            **{"TF_VAR_site": self.site},
            **{"TF_VAR_azrsa": self.bucket},
            **{"TF_VAR_bucket": self.bucket},
            **{"TF_VAR_prefix": self.prefix},
            **{"TF_VAR_china_deployment": self.china_deployment},
            **{"TF_CLI_ARGS": self.tf_cli_args},
            **{"AWS_REGION": self.region},
            **{"AZR_REGION": self.region},
            **{"REPO_PATH": self.repo_root},
            **{"REPO_PREFIX": self.repo_prefix},
            )
