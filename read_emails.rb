require "gmail"
require "pp"
require "yaml"

config = YAML.load(File.read("config.yml"))

Gmail.new(config["gmail"]["username"], config["gmail"]["password"]) do |gm|
  pp gm.inbox.emails(:from => config["go"]["email"]).map{|m| m.subject }
end

