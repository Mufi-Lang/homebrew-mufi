class Mufiz < Formula
  desc "Mufi Lang with Ziggyness"
  homepage "https://github.com/Mustafif/MufiZ"

  version = "0.9.0"

  url "https://github.com/Mustafif/MufiZ/releases/download/v#{version}/mufiz_#{version}_x86_64-linux.zip"
  sha256 "2e46ccdc9ee91d5655089eb6141c4a3e6cea4dcec3b887b9a46ec9e9762c55c8"
  license "GPL-2.0-only"

  # URL and SHA256 hash for ARM Mac
  on_macos do
    if Hardware::CPU.arm?
      url "https://github.com/Mustafif/MufiZ/releases/download/v#{version}/mufiz_#{version}_aarch64-macos.zip"
      sha256 "afb403aa864a673a60dc17f7dc25771db10c701b6d45fa17de99693937bac9b8"
    else
      # URL and SHA256 hash for Intel Mac
      url "https://github.com/Mustafif/MufiZ/releases/download/v#{version}/mufiz_#{version}_x86_64-macos.zip"
      sha256 "7ad890f559b8ddf4d105bab80c9c244d9d19c7e90e526192e809248a2c0d2bd0"
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
