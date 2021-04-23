from conans import ConanFile

class HelloWorld(ConanFile):
  name = "hello-world"
  version = "1.0.2"
  license = "MIT"
  url = "https://conan.io/center/hello-world"
  homepage = "https://github.com/cppf/hello-world"
  description = "A \"Hello, World!\" is an introductory computer program."
  topics = ("hello", "world", "template")
  exports_sources = "hello-world/*"
  no_copy_source = True

  def package(self):
    self.copy("*.h")

# picojson recipe
# url: https://github.com/conan-io/conan-center-index/blob/7a34d7b321de8455b1697c803a38086b208674e5/recipes/picojson/all/conanfile.py
# homepage: https://github.com/kazuho/picojson
# _source_subdir_name = "source_subdir"

# def source(self):
#   tools.get(**self.conan_data["sources"][self.version])
#   os.rename("picojson-{}".format(self.version), self._source_subdir_name)

# def package(self):
#   self.copy("{}.h".format(self.name), dst="include", src=self._source_subdir_name)
#   self.copy("LICENSE", dst="licenses", src=self._source_subdir_name)

# def package_info(self):
#   self.info.header_only()
