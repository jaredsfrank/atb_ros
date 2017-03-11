FILE(REMOVE_RECURSE
  "../msg_gen"
  "../msg_gen"
  "../src/nav/msg"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/nav/msg/__init__.py"
  "../src/nav/msg/_Num.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
