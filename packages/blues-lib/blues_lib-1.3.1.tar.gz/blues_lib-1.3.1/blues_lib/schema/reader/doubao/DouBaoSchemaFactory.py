import sys,re,os
from .gallery.DouBaoGallerySchema import DouBaoGallerySchema

sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from schema.reader.ReaderSchemaFactory import ReaderSchemaFactory

class DouBaoSchemaFactory(ReaderSchemaFactory):

  def create_gallery(self):
    return DouBaoGallerySchema()
