cd /root/.jenkins/workspace/Job1_GithubPull
pipreqs . --force

if grep -q "tensorflow" requirements.txt;
then  docker run -p 5000:5000 -v github_pull:/root/code -v dataset:/root/.keras -d --name DeepLearning dlcontainer:v4;
else  docker run -p 5000:5000 -v github_pull:/root/code -d --name MachieLearning mlcontainer:v1;  
fi
