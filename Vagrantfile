Vagrant.require_version ">= 1.7.0"

Vagrant.configure(2) do |config|

  config.vm.box = "hashicorp/precise64"
  
  
  config.ssh.insert_key = false


  config.vm.define :DB do |cfg|
        cfg.vm.network :private_network, ip: "10.0.0.10"
        cfg.vm.provider :virtualbox do |v|
            v.name = "DB"
        end
    end
    
  config.vm.define :App do |cfg|
        cfg.vm.network :private_network, ip: "10.0.0.11"
        cfg.vm.provider :virtualbox do |v|
            v.name = "App"
        end
    end

  config.vm.define :Web do |cfg|
        cfg.vm.network "forwarded_port", guest: 80, host: 9090
        cfg.vm.network :private_network, ip: "10.0.0.12"
        cfg.vm.provider :virtualbox do |v|
            v.name = "Web"
        end
    end

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "playbook.yaml"
    ansible.sudo = true
  end
end
