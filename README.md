# pyspark

Prerequisites:
Install JDK ( check spark version compatable )
Install Python
Install Spark
    Download spark distribution
    Store it into one of the mac folder locations
        Ex: /Users/{UserName}/Documents

    Edit ~/.bashrc
            export SPARK_HOME=/Users/{UserName}/Documents/spark-3.5.4-bin-hadoop3
            export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
        source ~/.bashrc

Apply spark-shell from terminal



Uninstall Java on mac os

Check whats's installed with ls -1 /Library/Java/JavaVirtualMachines

for example:
    $ ls -1 /Library/Java/JavaVirtualMachines
    jdk1.7.0_80.jdk
    jdk1.8.0_161.jdk
    jdk1.8.0_172.jdk
    jdk1.8.0_181.jdk
Remove the folder with
    sudo rm -R /Library/Java/JavaVirtualMachines/jdk1.8.0_161.jdk
Remove the entry in the OSX Installer database:
    first, find the entry name with pkgutil --pkgs | grep -i oracle
    for example:
        $ pkgutil --pkgs | grep -i oracle
            com.oracle.jdk8u161
            com.oracle.jre
            com.oracle.jdk7u80
            com.oracle.jdk8u181
            com.oracle.jdk8u152
    Then, remove the entry of the JVM you want to remove, e.g. com.oracle.jdk8u161, with
        sudo pkgutil --forget com.oracle.jdk8u161
    For those using jenv to manage different JVM/JDK versions, remember to remove the JDK from there too:
        jenv versions to see what is the name of the JDK you want to remove, then
        
        jenv remove oracle64-1.8.0.181`
        JDK oracle64-1.8.0.181 removed
