# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "emojime: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iemojime:/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(emojime_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg" NAME_WE)
add_custom_target(_emojime_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "emojime" "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(emojime
  "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/emojime
)

### Generating Services

### Generating Module File
_generate_module_cpp(emojime
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/emojime
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(emojime_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(emojime_generate_messages emojime_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg" NAME_WE)
add_dependencies(emojime_generate_messages_cpp _emojime_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(emojime_gencpp)
add_dependencies(emojime_gencpp emojime_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS emojime_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(emojime
  "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/emojime
)

### Generating Services

### Generating Module File
_generate_module_eus(emojime
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/emojime
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(emojime_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(emojime_generate_messages emojime_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg" NAME_WE)
add_dependencies(emojime_generate_messages_eus _emojime_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(emojime_geneus)
add_dependencies(emojime_geneus emojime_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS emojime_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(emojime
  "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/emojime
)

### Generating Services

### Generating Module File
_generate_module_lisp(emojime
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/emojime
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(emojime_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(emojime_generate_messages emojime_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg" NAME_WE)
add_dependencies(emojime_generate_messages_lisp _emojime_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(emojime_genlisp)
add_dependencies(emojime_genlisp emojime_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS emojime_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(emojime
  "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/emojime
)

### Generating Services

### Generating Module File
_generate_module_nodejs(emojime
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/emojime
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(emojime_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(emojime_generate_messages emojime_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg" NAME_WE)
add_dependencies(emojime_generate_messages_nodejs _emojime_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(emojime_gennodejs)
add_dependencies(emojime_gennodejs emojime_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS emojime_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(emojime
  "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/emojime
)

### Generating Services

### Generating Module File
_generate_module_py(emojime
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/emojime
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(emojime_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(emojime_generate_messages emojime_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tepic/Documents/Cloud/NextCloud/_M21/Multimodal Interaction for Ubiquitous Computers/[06] Git-Codes/emojiMe/workspace/src/emojime/msg/ImageArray.msg" NAME_WE)
add_dependencies(emojime_generate_messages_py _emojime_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(emojime_genpy)
add_dependencies(emojime_genpy emojime_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS emojime_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/emojime)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/emojime
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(emojime_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(emojime_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/emojime)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/emojime
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(emojime_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(emojime_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/emojime)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/emojime
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(emojime_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(emojime_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/emojime)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/emojime
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(emojime_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(emojime_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/emojime)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/emojime\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/emojime
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(emojime_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(emojime_generate_messages_py sensor_msgs_generate_messages_py)
endif()
