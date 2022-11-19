import shutil
import os


def movefiles():

    try:
        cwd = os.getcwd()
        source = cwd + "/frontend/templates"
        destination = cwd + "/app"

        try:
            shutil.rmtree(cwd+"/app/_next/static/")
            shutil.rmtree(cwd+"/app/templates")
        except:
            print(" No action needed")

        # os.mkdir(cwd + "/app/_next/static")
        dest = shutil.move(source, destination, copy_function=shutil.copytree)

        source2 = cwd + "/app/templates/static"
        destination2 = cwd + "/app/_next/"

        dest2 = shutil.move(source2, destination2,
                            copy_function=shutil.copytree)
        print(dest2)
    except Exception as inst:
        print(f"Error while tranfering {inst.args}")


movefiles()
