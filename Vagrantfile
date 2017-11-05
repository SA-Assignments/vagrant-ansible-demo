Vagrant.require_version ">= 1.7.0"

Vagrant.configure(2) do |config|

  config.vm.box = "hashicorp/precise64"
  
  # config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "forwarded_port", guest: 5000, host: 7070
  # config.vm.network "forwarded_port", guest: 80, host: 6060  
  
  config.ssh.insert_key = false


  config.vm.define :DB do |cfg|
        # cfg.vm.network :public_network, bridge: "wlan0" # , ip: "192.168.33.20"
        # cfg.vm.network "forwarded_port", guest: 3306, host: 3306
        cfg.vm.network :private_network, ip: "10.0.0.10"
        cfg.vm.provider :virtualbox do |v|
            v.name = "DB"
        end
    end
    
  config.vm.define :App do |cfg|
        # cfg.vm.network :public_network, bridge: "wlan0" # , ip: "192.168.33.15"
        # cfg.vm.network "forwarded_port", guest: 5000, host: 17070
        cfg.vm.network :private_network, ip: "10.0.0.11"
        cfg.vm.provider :virtualbox do |v|
            v.name = "App"
        end
    end

  config.vm.define :Web do |cfg|
        # cfg.vm.network :public_network , bridge: "wlan0" # , ip: "192.168.33.10"
        cfg.vm.network "forwarded_port", guest: 80, host: 9090
        cfg.vm.network :private_network, ip: "10.0.0.12"
        cfg.vm.provider :virtualbox do |v|
            v.name = "Web"
        end
    end

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yaml"
    # ansible.inventory_file = "group_vars/inventory"
    ansible.sudo = true
  end
end
