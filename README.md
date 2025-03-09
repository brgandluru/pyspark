# pyspark

Prerequisites:
Install JDK ( check spark version compatable.. here it is jdk21 )
Install Python3
Visual studio code


Installation of apache-spark:
        brew install apache-spark

    set environment variables:
        export SPARK_HOME=/opt/homebrew/Cellar/apache-spark/3.5.5/libexec
        export PATH=$SPARK_HOME/bin:$PATH

    Go to below location in VisualStudioCode:

        code -> preference -> setting -> {search for 'ENV: Osx'} -> edit the setting.json
        
        update settings.json with below 

        "terminal.integrated.env.osx": {
             "SPARK_HOME": "/usr/local/Cellar/apache-spark/3.0.0/libexec"
            }
        
        Restart VisualStudioCode and create virtual machine using requirements.txt from project folder

        pip install -r requirements.txt

