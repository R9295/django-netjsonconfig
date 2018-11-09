import netjsonconfig

class CoovaConverter(netjsonconfig.backends.openwrt.converters.base.OpenWrtConverter):
    netjson_key = 'chilli'
    _uci_types = ['chilli']
    def to_intermediate_loop(self, block, result, index=None):
        if block:
            block.update({
                '.type': 'chilli',
                '.name': 'chilli'
            })
        result['chilli'] = [self.sorted_dict(block)]
        return result

class CoovaPlugin(object):
    key = 'chilli'
    converter = CoovaConverter
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
             "disabled": {"type": "integer"},
             "uamsecret": {"type": "string"},
         },
    }
