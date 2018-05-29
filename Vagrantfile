# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"

  config.vm.network "forwarded_port", guest: 58080, host: 8080
  # config.vm.network "forwarded_port", guest: 8000, host: 8000

  # config.vm.network "private_network", ip: "192.168.33.10"


  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    echo "SETUP epel yum repo....."
    sudo yum -y install epel-release
    sudo yum --enablerepo=epel -y install epel-release

    sudo yum update -y
    sudo yum install -y git wget.x86_64 zlib.x86_64

    # Compilers and related tools:
    sudo yum groupinstall -y "development tools"

    # Libraries needed during compilation to enable all features of Python:
    sudo yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel expat-devel

    echo "INSTALL Python3....."
    mkdir python3
    cd python3

    wget -c https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
    md5sum -c <<<"2c68846471994897278364fc18730dd9  Python-3.6.2.tar.xz"

    tar -xJf Python-3.6.2.tar.xz
    
    cd Python-3.6.2

    # the following errored, but were recommendations.
    # ./configure \
    #   --prefix=/usr/local \
    #   --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib" \
    #   --enable-optimizations \
    #   --with-lto
    
    ./configure --prefix=/usr/local --enable-shared --enable-optimizations

    sudo make -j 2
    sudo make altinstall
    
    echo "Strip the Python 3.6 binary....."
    strip /usr/local/lib/libpython3.6m.so.1.0

    echo "export LD_LIBRARY_PATH=/usr/local/lib" >> /home/vagrant/.bashrc
    echo 'alias python="/usr/local/bin/python3.6"' >> /home/vagrant/.bashrc

    cd /home/vagrant

    sudo rm -rf /home/vagrant/python3

    # at this point we can set up the venv

  SHELL

  # config.vm.synced_folder "../data", "/vagrant_data"
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"

end
