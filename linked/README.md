# Linked

This folder contains the symblic links that create the final structure of the
desired deployed package.

For a complete explanation of why this is required, please consult the
README.md file in the root of this repository.

## Structure

For `<service>` folder within the `/services` folder, we create the following
here:

    ln -s ../core <service>
    ln -s ../services/<service> <service>/<service>
    ln -s ../services/service_requirements.txt <service>/service_requirements.txt

This creates a singlke, runnable project that merger both the core and the 
service without duplicating code.
