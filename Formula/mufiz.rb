class Mufiz < Formula
  desc "Mufi Lang with Ziggyness"
  homepage "https://github.com/Mustafif/MufiZ"

  version = "0.7.0"

  url "https://github.com/Mustafif/MufiZ/releases/download/v#{version}/mufiz_#{version}_x86_64-linux.zip"
  sha256 "d46045e72c0fd81ec31be5f568c35e95dc09a5d6778e0c51639db455bda14199"
  license "GPL-2.0-only"

  # URL and SHA256 hash for ARM Mac
  on_macos do
    if Hardware::CPU.arm?
      url "https://github.com/Mustafif/MufiZ/releases/download/v#{version}/mufiz_#{version}_aarch64-macos.zip"
      sha256 "7fb74348c27348d1e2648063820f4fb56db4c3d468a1759f6ca69d7758baab21"
    else
      # URL and SHA256 hash for Intel Mac
      url "https://github.com/Mustafif/MufiZ/releases/download/v#{version}/mufiz_#{version}_x86_64-macos.zip"
      sha256 "d4f8669ac632f40a5a2f0a9d1b929319f756e00175d7896e9c6775be3f887dd1"
    end
  end

  def install
    # Move the binary to /usr/local/bin
    bin.install "mufiz"
  end

  test do
    # Add a simple test here if possible
    system "#{bin}/mufiz", "--version"
  end
end
