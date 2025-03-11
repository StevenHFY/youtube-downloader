ZSH_DISABLE_COMPFIX=true
export ZSH="/Users/huifengyao/.oh-my-zsh"
export PATH="/usr/local/mysql/bin:$PATH"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/huifengyao/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/huifengyao/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/huifengyao/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/huifengyao/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

#JAVA
JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.8.0_221.jdk/Contents/Home"
CLASS_HOME="$JAVA_HOME/lib"
PATH=".;$PATH:$JAVA_HOME/bin"
export JAVA_HOME
export CLASS_HOME
export PATH

#MAVEN
MAVEN_HOME=/usr/local/apache-maven-3.6.3
PATH=${PATH}:${MAVEN_HOME}/bin
export MAVEN_HOME

ZSH_THEME="cloud"
plugins=(git)
source $ZSH/oh-my-zsh.sh

export https_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Set conda environment path
export PATH="/Users/huifengyao/anaconda3/envs/py38/bin:$PATH" 