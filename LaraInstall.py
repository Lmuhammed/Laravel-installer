import os
clear_command="clear"
LaravelCrucialFiles=[
    "composer.json",
    "package.json",
    "artisan",
]
for file in LaravelCrucialFiles:
    #Check if files exist
    if not (os.path.exists(file)):
        print(f"{file} does not exist.")
        exit(22)
    else:
        commands=[
            "composer install",
            "npm install",
            "cp ./.env.example ./.env",
            "php artisan key:generate",
            "php artisan migrate",
        ]
        for command in commands:
            #execute commands
            return_value = os.system(command)
            if return_value == 0:
                continue
            else:
                print(f"{Command} failed with return value:", return_value)
                break
        #Ask to start local development server               
        artisan_serve="php artisan serve"
        os.system(clear_command)
        while True:
                opt = input("Run the local development server (y/n): ")
                opt=opt.lower()
                if opt == "y":
                    os.system(clear_command)
                    os.system(artisan_serve)
                    break
                elif opt == "n":
                    print("Bye ...")
                    exit(0)
                else:
                    print("Invalid option:", opt)
                    break
