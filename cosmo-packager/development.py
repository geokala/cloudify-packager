########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

# WORKING ENVIRONMENT
ENV = "develop"
# base packager repo dir
PACKAGER_BASE = "/cosmo-packager/cosmo-packager"
# directory for bootstrap/download/removal/package scripts - if applicable
PACKAGER_SCRIPTS_DIR = "/cosmo-packager/cosmo-packager/package-scripts"
# package configurations directory
PACKAGER_CONF_DIR = "/cosmo-packager/cosmo-packager/package-configuration"
# directory which contains configuration for all modules
PACKAGER_TEMPLATE_DIR = "/cosmo-packager/cosmo-packager/package-templates"
# temporary directory to which items are downloaded and packages are created.
PACKAGES_DIR = "/packages"
# final directory to put the created packages in.
COMPONENTS_BOOTSTRAP_DIR = "/cloudify3-components"
CODE_BOOTSTRAP_DIR = "/cloudify3"
# directory for cosmo modules and virtual environments
VIRTUALENVS_DIR = "/opt"
# specific package configuration
PACKAGES = {
    "cloudify3": {
        "name": "cloudify3",
        "version": "3.0.0",
        "depends": ['cloudify3-components'],
        "bootstrap_dir": "/cloudify",
        "package_dir": "%s" % CODE_BOOTSTRAP_DIR,
        "conf_dir": "%s" % PACKAGER_CONF_DIR,
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/cloudify3-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "cloudify3-bootstrap.template",
        "bootstrap_log": "/var/log/cloudify3-bootstrap.log",
        "req_free_mem": "10000",
        "req_free_disk": "5",
        "req_cpu_cores": "1",
        "req_arch": "x86_64",
        "req_os": "precise"
    },
    "cloudify3-components": {
        "name": "cloudify3-components",
        "version": "3.0.0",
        "bootstrap_dir": "/cloudify",
        "package_dir": "%s" % COMPONENTS_BOOTSTRAP_DIR,
        "conf_dir": "%s" % PACKAGER_CONF_DIR,
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/cloudify3-components-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "cloudify3-components-bootstrap.template",
        "bootstrap_log": "/var/log/cloudify3-bootstrap.log",
        "req_free_mem": "10000",
        "req_free_disk": "5",
        "req_cpu_cores": "1",
        "req_arch": "x86_64",
        "req_os": "precise"
    },
    "python-pip": {
        "name": "python-pip",
        "version": "1.0",
        "bootstrap_dir": "%s/python-pip/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/python-pip" % PACKAGES_DIR
    },
    "logstash": {
        "name": "logstash",
        "version": "1.3.2",
        "source_url": "https://download.elasticsearch.org/logstash/logstash/logstash-1.3.2-flatjar.jar",
        "depends": ['openjdk-7-jdk'],
        "bootstrap_dir": "%s/logstash/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/logstash" % PACKAGES_DIR,
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/logstash-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "logstash-bootstrap.template"
    },
    "elasticsearch": {
        "name": "elasticsearch",
        "version": "0.90.9",
        "source_url": "https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.9.tar.gz",
        "depends": ['openjdk-7-jdk'],
        "bootstrap_dir": "%s/elasticsearch/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/elasticsearch" % PACKAGES_DIR,
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/elasticsearch-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "elasticsearch-bootstrap.template"
    },
    "kibana3": {
        "name": "kibana3",
        "version": "3.0.0milestone4",
        "source_url": "https://download.elasticsearch.org/kibana/kibana/kibana-3.0.0milestone4.tar.gz",
        "depends": ['openjdk-7-jdk', 'logstash', 'elasticsearch'],
        "bootstrap_dir": "%s/kibana3/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/kibana3" % PACKAGES_DIR,
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/kibana-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "kibana-bootstrap.template"
    },
    "nginx": {
        "name": "nginx",
        "version": "1.5.8",
        "source_url": "http://nginx.org/packages/mainline/ubuntu/ precise nginx",
        "source_key": "http://nginx.org/keys/nginx_signing.key",
        "key_file": "nginx_signing.key",
        "bootstrap_dir": "%s/nginx/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/nginx" % PACKAGES_DIR
    },
    "rabbitmq-server": {
        "name": "rabbitmq-server",
        "version": "0.0.1",
        "source_url": "http://www.rabbitmq.com/debian/ testing main",
        "source_key": "http://www.rabbitmq.com/rabbitmq-signing-key-public.asc",
        "key_file": "rabbitmq-signing-key-public.asc",
        'erlang': "erlang-nox",
        "bootstrap_dir": "%s/rabbitmq-server/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/rabbitmq-server" % PACKAGES_DIR
    },
    "riemann": {
        "name": "riemann",
        "version": "0.2.2",
        "source_url": "http://aphyr.com/riemann/riemann_0.2.2_all.deb",
        "depends": ['openjdk-7-jdk'],
        "bootstrap_dir": "%s/riemann/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/riemann" % PACKAGES_DIR
    },
    "nodejs": {
        "name": "nodejs",
        "version": "0.0.1",
        "source_url": "ppa:chris-lea/node.js",
        "bootstrap_dir": "%s/nodejs/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/nodejs" % PACKAGES_DIR,
        "prereqs": ['python-software-properties', 'g++', 'make', 'python']
    },
    "openjdk-7-jdk": {
        "name": "openjdk-7-jdk",
        "version": "0.0.1",
        "bootstrap_dir": "%s/openjdk-7-jdk/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/openjdk-7-jdk" % PACKAGES_DIR
    },
    "virtualenv": {
        "name": "virtualenv",
        "version": "1.10.1",
        "bootstrap_dir": "%s/virtualenv/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/virtualenv" % PACKAGES_DIR,
        "modules": ['virtualenv==1.10.1'],
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/virtualenv-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "virtualenv-bootstrap.template"
    },
    "graphite": {
        "name": "graphite",
        "version": "0.9.12",
        "bootstrap_dir": "%s/graphite/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/graphite" % VIRTUALENVS_DIR,
        "modules": ['carbon==0.9.10', 'whisper==0.9.12', 'graphite-web==0.9.12'],
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/graphite-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "graphite-bootstrap.template"
    },
    "dsl-parser-modules": {
        "name": "dsl-parser-modules",
        "version": "0.0.1",
        "bootstrap_dir": "%s/dsl-parser-modules/" % CODE_BOOTSTRAP_DIR,
        "package_dir": "%s/dsl-parser-modules" % PACKAGES_DIR,
        "virtualenv": "%s/cosmo-manager" % VIRTUALENVS_DIR,
        "modules": ['pyyaml', 'jsonschema', 'pika', 'https://github.com/CloudifySource/cosmo-plugin-dsl-parser/archive/develop.tar.gz'],
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/dsl-parser-modules-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "python-modules-bootstrap.template"
    },
    "manager-modules": {
        "name": "manager-modules",
        "version": "0.0.1",
        "bootstrap_dir": "%s/manager-modules/" % CODE_BOOTSTRAP_DIR,
        "package_dir": "%s/manager-modules" % PACKAGES_DIR,
        "virtualenv": "%s/cosmo-manager" % VIRTUALENVS_DIR,
        "modules": ['Flask', 'flask-restful', 'flask-restful-swagger', 'requests', 'bernhard', 'pika'],
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/manager-modules-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "python-modules-bootstrap.template"
    },
    "manager": {
        "name": "manager",
        "version": "0.0.1",
        "source_url": "https://github.com/CloudifySource/cosmo-manager/archive/develop.tar.gz",
        "depends": ['openjdk-7-jdk'],
        "bootstrap_dir": "%s/manager/" % CODE_BOOTSTRAP_DIR,
        "package_dir": "%s/manager" % VIRTUALENVS_DIR,
        "virtualenv": "%s/manager" % VIRTUALENVS_DIR,
        "modules": ['%s/manager/cosmo-manager-develop/manager-rest/' % VIRTUALENVS_DIR],
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/manager-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "manager-bootstrap.template"
    },
    "celery": {
        "name": "celery",
        "version": "0.0.1",
        "bootstrap_dir": "%s/celery/" % CODE_BOOTSTRAP_DIR,
        "package_dir": "%s/celery" % VIRTUALENVS_DIR,
        "virtualenv": "%s/celery" % VIRTUALENVS_DIR,
        "modules": ['billiard==2.7.3.28', 'celery==3.0.24', 'bernhard', 'pika',
                    'https://github.com/CloudifySource/cosmo-plugin-agent-installer/archive/develop.tar.gz',
                    'https://github.com/CloudifySource/cosmo-plugin-openstack-provisioner/archive/develop.tar.gz',
                    'https://github.com/CloudifySource/cosmo-plugin-plugin-installer/archive/develop.tar.gz',
                    'https://github.com/CloudifySource/cosmo-plugin-riemann-configurer/archive/develop.tar.gz'],
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/celery-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "celery-bootstrap.template"
    },
    "bundler": {
        "name": "bundler",
        "version": "0.0.1",
        "bootstrap_dir": "%s/bundler/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/bundler" % PACKAGES_DIR,
        "gems": ['bundler'],
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/bundler-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "ruby-gems-bootstrap.template"
    },
    "workflow-jruby": {
        "name": "workflow-jruby",
        "version": "1.7.3",
        "source_url": "http://jruby.org.s3.amazonaws.com/downloads/1.7.3/jruby-bin-1.7.3.tar.gz",
        "depends": ['openjdk-7-jdk'],
        "gemfile_source_url": "https://github.com/CloudifySource/cosmo-manager/archive/develop.tar.gz",
        "gemfile_location": "%s/workflow-jruby/cosmo-manager-develop/workflow-service/Gemfile" % PACKAGES_DIR,
        "bootstrap_dir": "%s/workflow-jruby/" % CODE_BOOTSTRAP_DIR,
        "package_dir": "%s/workflow-jruby" % PACKAGES_DIR,
        "bin_home_dir": "jruby-1.7.3/bin",
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/workflow-jruby-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "workflow-jruby-bootstrap.template"
    },
    "jruby": {
        "name": "jruby",
        "version": "1.7.3",
        "source_url": "http://jruby.org.s3.amazonaws.com/downloads/1.7.3/jruby-bin-1.7.3.tar.gz",
        "bootstrap_dir": "%s/jruby/" % COMPONENTS_BOOTSTRAP_DIR,
        "package_dir": "%s/jruby" % PACKAGES_DIR,
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/jruby-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "jruby-bootstrap.template"
    },
    "workflow-gems": {
        "name": "workflow-gems",
        "version": "0.0.1",
        "source_url": "https://github.com/CloudifySource/cosmo-manager/archive/develop.tar.gz",
        "bootstrap_dir": "%s/workflow-gems/" % CODE_BOOTSTRAP_DIR,
        "package_dir": "%s/workflow-gems" % PACKAGES_DIR,
        "virtualenv": VIRTUALENVS_DIR,
        "gems": ['rufus-scheduler -v 2.0.24', 'sinatra -v 1.4.4', 'ruby_parser -v 3.1', 'ruby_parser -v 2.3', 'ruote -v 2.3.0.2', 'rest-client -v 1.6.7'],
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/workflow-gems-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "ruby-gems-bootstrap.template"
    },
    "cosmo-ui": {
        "name": "cosmo-ui",
        "version": "1.0.0",
        "source_url": "http://builds.gsdev.info/cosmo-ui/1.0.0/cosmo-ui-1.0.0-latest.tgz",
        "depends": ['nodejs'],
        "bootstrap_dir": "%s/cosmo-ui/" % CODE_BOOTSTRAP_DIR,
        "package_dir": "%s/cosmo-ui" % PACKAGES_DIR,
        "virtualenv": "%s/cosmo-ui" % VIRTUALENVS_DIR,
        "src_package_type": "dir",
        "dst_package_type": "deb",
        "bootstrap_script": "%s/cosmo-ui-bootstrap.sh" % PACKAGER_SCRIPTS_DIR,
        "bootstrap_template": "cosmo-ui-bootstrap.template"
    }
}
# logger configuration
PACKAGER_LOGGER = {
    "version": 1,
    "formatters": {
        "file": {
            "format": "%(asctime)s %(levelname)s - %(message)s"
        },
        "console": {
            "format": "########## %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "file",
            "level": "DEBUG",
            "filename": "/var/log/packager/packager.log",
            "maxBytes": "5000000",
            "backupCount": "20"
        },
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "console"
        }
    },
    "loggers": {
        "packager": {
            "level": "DEBUG",
            "handlers": ["file", "console"]
        }
    }
}
# event broker config (if applicable)
RABBITMQ_HOST = '10.0.0.3'
# RABBITMQ_HOST = 'installcosmo.gsdev.info'
# queue name for packager events
RABBITMQ_QUEUE = 'hello'
# routing key..
RABBITMQ_ROUTING_KEY = 'packager'
# broker exchange
RABBITMQ_EXCHANGE = ''
