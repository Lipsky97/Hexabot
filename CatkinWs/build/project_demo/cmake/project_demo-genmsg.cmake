# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "project_demo: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iproject_demo:/home/lipsky/MyDsk/plug/src/project_demo/msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(project_demo_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg" NAME_WE)
add_custom_target(_project_demo_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "project_demo" "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(project_demo
  "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/project_demo
)

### Generating Services

### Generating Module File
_generate_module_cpp(project_demo
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/project_demo
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(project_demo_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(project_demo_generate_messages project_demo_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg" NAME_WE)
add_dependencies(project_demo_generate_messages_cpp _project_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(project_demo_gencpp)
add_dependencies(project_demo_gencpp project_demo_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS project_demo_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(project_demo
  "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/project_demo
)

### Generating Services

### Generating Module File
_generate_module_eus(project_demo
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/project_demo
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(project_demo_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(project_demo_generate_messages project_demo_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg" NAME_WE)
add_dependencies(project_demo_generate_messages_eus _project_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(project_demo_geneus)
add_dependencies(project_demo_geneus project_demo_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS project_demo_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(project_demo
  "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/project_demo
)

### Generating Services

### Generating Module File
_generate_module_lisp(project_demo
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/project_demo
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(project_demo_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(project_demo_generate_messages project_demo_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg" NAME_WE)
add_dependencies(project_demo_generate_messages_lisp _project_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(project_demo_genlisp)
add_dependencies(project_demo_genlisp project_demo_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS project_demo_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(project_demo
  "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/project_demo
)

### Generating Services

### Generating Module File
_generate_module_nodejs(project_demo
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/project_demo
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(project_demo_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(project_demo_generate_messages project_demo_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg" NAME_WE)
add_dependencies(project_demo_generate_messages_nodejs _project_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(project_demo_gennodejs)
add_dependencies(project_demo_gennodejs project_demo_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS project_demo_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(project_demo
  "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/project_demo
)

### Generating Services

### Generating Module File
_generate_module_py(project_demo
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/project_demo
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(project_demo_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(project_demo_generate_messages project_demo_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lipsky/MyDsk/plug/src/project_demo/msg/Leg.msg" NAME_WE)
add_dependencies(project_demo_generate_messages_py _project_demo_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(project_demo_genpy)
add_dependencies(project_demo_genpy project_demo_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS project_demo_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/project_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/project_demo
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(project_demo_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(project_demo_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/project_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/project_demo
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(project_demo_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(project_demo_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/project_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/project_demo
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(project_demo_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(project_demo_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/project_demo)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/project_demo
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(project_demo_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(project_demo_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/project_demo)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/project_demo\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/project_demo
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(project_demo_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(project_demo_generate_messages_py std_msgs_generate_messages_py)
endif()
