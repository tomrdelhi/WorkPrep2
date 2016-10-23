from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Metrics(models.Model):
	id_val = models.AutoField(primary_key = True)
	extension = models.CharField(max_length=250)
	timestamp = models.DateTimeField(auto_now_add=True)
	type_val = models.CharField(max_length = 250)
	label = models.CharField(max_length=250)
	action = models.CharField(max_length=250)
	value = models.IntegerField()
	location = models.CharField(max_length=250)
	#extra
	ip_address = models.IntegerField()
	def __str__(self):
		return '{0} {1} {2}'.format(self.id_val, self.label, self.timestamp)

#CREATE TABLE `metrics` (
#  `id` int(11) NOT NULL AUTO_INCREMENT,
#  `extension` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
#  `timestamp` datetime NOT NULL,
#  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
#  `label` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
#  `action` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
#  `value` int(11) DEFAULT NULL,
#  `location` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
#  `extra` json DEFAULT NULL,
#  `ip_address` int(4) unsigned DEFAULT NULL,
#  PRIMARY KEY (`id`,`extension`),
#  KEY `extension_date_index` (`extension`(16),`timestamp`)
#) ENGINE=InnoDB AUTO_INCREMENT=58853103 DEFAULT CHARSET=latin1
#/*!50100 PARTITION BY KEY (extension) */ |