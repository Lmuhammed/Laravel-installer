try:
    import os
except ImportError:
    print("In order for LARAVEL to work properly this script requires : 'os' module")
    raise SystemExit(1)

#var 
clear_command="clear"
LaravelCrucialFiles=[
    "composer.json",
    "package.json",
    "artisan",
]

commands=[
            "composer install",
            "npm install",
            "cp ./.env.example ./.env",
            "php artisan key:generate",
            "php artisan migrate",
]

artisan_serve="php artisan serve"

#end 

for file in LaravelCrucialFiles:
    #Check if files exist
    if not (os.path.exists(file)):
        print(f"In order for LARAVEL to work properly,the project folder needs to have several files, including the following: {file}")
        exit(2)

for command in commands:
#execute commands
    return_value = os.system(command)
    if return_value == 0:
        continue
    else:
        print(f"{command} failed with return value:", return_value)
        break
    #Ask to start local development server               
    os.system(clear_command)
    while True:
        opt = input("Run the local development server (y/n): ")
        opt=opt.lower()
        if opt == "y":
            os.system(artisan_serve)
            break
        elif opt == "n":
            print("Bye ...")
            exit(2)
        else:
            print(f"unknown command : {opt} ")
