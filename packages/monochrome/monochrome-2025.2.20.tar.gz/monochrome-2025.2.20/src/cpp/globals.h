#pragma once

#include <string>
#include <optional>
#include <utility>
#include <memory>
#include <variant>
#include <vector>

#include <asio.hpp>
#include <asio/thread_pool.hpp>
#include <fmt/format.h>

#include "utils/vectors.h"
#include "utils/definitions.h"

namespace global {
  class Message;

  extern std::vector<Message> messages;
  extern std::string tcp_host;
  extern short tcp_port;
  extern asio::thread_pool thread_pool;

  class Message {
   public:
    bool show = true;
    std::string msg;
    int id = 0;

    Message(std::string msg);
  };

  template <typename... Args>
  inline void new_ui_message(const char *fmt, Args &&...args) {
    const std::string msg = fmt::format(fmt, std::forward<Args>(args)...);
    messages.emplace_back(msg);
    std::string prefix("ERROR");
    if (msg.compare(0, prefix.size(), prefix)) {
      fmt::print(stderr, msg + "\n");
    } else {
      fmt::print(msg + "\n");
    }
  }

  template <typename... Args>
  inline void new_ui_message(const std::string &fmt, Args &&...args) {
    return new_ui_message(fmt.c_str(), std::forward<Args>(args)...);
  }

  void add_file_to_load(const std::string &file);

  std::optional<std::string> get_file_to_load();

  struct RawArray3MetaData {
    int nx = -1;
    int ny = -1;
    int nt = -1;

    std::string name;
    float duration = 0;  // in seconds
    float fps      = 0;  // in Hz
    std::string date;
    std::string comment;
    std::optional<BitRange> bitrange                          = std::nullopt;
    std::optional<ColorMap> cmap                              = std::nullopt;
    std::optional<float> vmin                                 = std::nullopt;
    std::optional<float> vmax                                 = std::nullopt;
    std::optional<std::string> parentName                     = std::nullopt;
    std::optional<OpacityFunction> opacity                    = std::nullopt;
    std::vector<std::pair<std::string, std::string>> metaData = {};
    std::optional<Vec4f> color                                = std::nullopt;

    bool is_flowfield = false;
  };

  struct RemoteCommand {
    virtual ~RemoteCommand() = default;
  };
  void add_remote_command(std::shared_ptr<RemoteCommand> cmd);
  std::optional<std::shared_ptr<RemoteCommand>> get_remote_command();

  struct LoadFileCommand : RemoteCommand {
    LoadFileCommand(const std::string &filename_) : filename(filename_) {}
    std::string filename;
  };
  class RawArray3 : public RemoteCommand {
   private:
    RawArray3() = default;

   public:
    RawArray3MetaData meta;
    std::variant<std::vector<float>, std::vector<uint8_t>, std::vector<uint16_t>> data;

    template <typename T>
    static std::shared_ptr<RawArray3> create(RawArray3MetaData metadata_, std::size_t data_size) {
      auto a  = std::shared_ptr<RawArray3>(new RawArray3);
      a->meta = std::move(metadata_);
      a->data = std::vector<T>(data_size);
      return a;
    }

    std::size_t size() const {
      return std::visit([](auto &v) { return v.size(); }, data);
    }
  };

  struct PointsVideo : RemoteCommand {
    std::string name;
    std::string parent_name;
    std::vector<std::vector<float>> data;
    Vec4f color      = {0, 0, 0, 0};
    float point_size = -1;
    bool show        = true;

    void assign_next_color(unsigned color_count) {
      // List of colors to cycle through
      const std::array<Vec4f, 6> cycle_list = {{
          {0, 0, 0, 1},
          {1, 1, 1, 1},
          {228 / 255.f, 26 / 255.f, 28 / 255.f, 1},
          {55 / 255.f, 126 / 255.f, 184 / 255.f, 1},
          {77 / 255.f, 175 / 255.f, 74 / 255.f, 1},
          {152 / 255.f, 78 / 255.f, 163 / 255.f, 1},
      }};

      if (color_count >= cycle_list.size()) {
        color_count %= cycle_list.size();
      }
      color = cycle_list.at(color_count);
    }
  };

  struct ExportVideoCommand : RemoteCommand {
    std::string recording;
    std::string filename;
    std::string description;
    int t_start = 0;
    int t_end   = -1;
    int fps     = 30;
    bool close_after_completion = false;
  };

  struct CloseVideoCommand : RemoteCommand {
    std::string recording;
    CloseVideoCommand(std::string recording_) : recording(recording_) {}
  };

  // special case for file loading to allow for double-clicking files in the file browser
  void add_file_to_load(const std::string &filename);

  // Initiate shutdown of the application
  void quit(int code = 0);
}  // namespace global