#!/bin/bash
artisan=artisan
composer=composer.json
packege=package.json
if [ ! -d "$artisan" ] && [ ! -d "$composer" ]  && [ ! -d "$packege" ]; then
echo "This is Not a Laravel project "
echo "One or all this crucial files dose not exists :"
echo "artisan ,composer.json ,package.json"
echo "Please verifiy the location or reclone the repo"
exit
fi
#commands 
composer="composer install" 
npm="npm install" 
env="cp .env.exemple .env" 
key="php artisan key:generate"
migration="php artisan migrate" 
for command in $composer $npm $env $key $migration
do
  $command
  if [ $? == 0 ]
  then
    continue
  else echo "Sorry ,an error accurd while executing the command : $command"
  fi
done
#npm dev / build & artisan serve 
PS3="Do you want to lunuch the app after installing the deps ? "
select opt in Yes No; do
  case $opt in
    Yes)
    lunch_server=true
    break
    ;;
    No)
    lunch_server=false
    break
    ;;
    *) 
    echo "Invalid option : $REPLY"
    break
    ;;
  esac
done

PS3="For the node deps , use npm run dev or npm run build ? "
select opt in Dev Build; do
  case $opt in
    Dev)
    npm_run_dev=true
    break
    ;;
    Build)
    npm_run_build=true
    break
    ;;
    *) 
    echo "Invalid option : $REPLY"
    break
    ;;
  esac
done

artisan_serve="php artisan serve"
dev="npm run dev"
build="npm run build"
if [ $lunch_server ] && [ $npm_run_dev ]
then
$artisan_serve && $dev
else if [ $lunch_server ] && [ $npm_run_build ] 
then
$artisan_serve && $build
fi
fi
