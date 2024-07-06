try:
    import os
except ImportError:
    print("In order for this script to work properly the 'os' module required")
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
programsToCheck = set(element.split()[0] for element in commands)
artisan_serve="php artisan serve"

#end vars

#func

def program_installed(program_name):
    no_output="> /dev/null"
    command = f"which {program_name} {no_output}"
    return os.system(command) == 0

for file in LaravelCrucialFiles:
    #Check if files exist
    if not (os.path.exists(file)):
        print(f"In order for LARAVEL to work properly,the project folder needs to have several files, including the following: {file}")
        exit(1)

for program in programsToCheck:
    if not program_installed(program):
        print(f"In order for LARAVEL to work properly, Some programs must be installed :")
        print(f"{program} is not installed")
        exist(1)

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
            exit(1)
        else:
            print(f"unknown command : {opt} ")
