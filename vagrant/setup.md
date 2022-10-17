# Vagrant

- It is essentially a VM

- install from website: https://www.vagrantup.com/downloads

- Syntax similar to Terraform as it is from Hashicorp

Set up of linux vm

```bash
vagrant init ubuntu/trusty64
```

- Open up Vagrantfile and edit config if you want:
    -  delete all commented lines and make own setup

A provider is needed:

- Use VirtualBox
    - Download virtual box:
        - https://www.virtualbox.org/wiki/Downloads
        - Has to be the correct verrsion
        

```
vagrant up
```

Go into the VM:

```
vagrant ssh
```

If vagrant asks for password, it is 'vagrant'.

Now in a vm. The files in the working directory gets saved onto this vm. To find it, 

```
cd /
cd vagrant/
```
In this folder, the files thats saved in the same folder as vagrant will be there. It also updates in real time.

To turn off vagrant vm

- CTRL-D

To destroy Vagrant 

```
vagrant destroy
```

On virtual box, the VM is now gone.