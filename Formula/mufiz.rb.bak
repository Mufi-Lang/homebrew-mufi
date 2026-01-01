class Mufiz < Formula
  desc "Mufi Lang with Ziggyness"
  homepage "https://github.com/Mustafif/MufiZ"

  version = "0.9.0"

  url "https://github.com/Mustafif/MufiZ/releases/download/v0.9.0/mufiz_0.9.0_x86_64-linux.zip"
  sha256 "237e801e5824ef2c5ab53a08136b02531bd2f8e8666ca41f3f0c47d35e96925a"
  license "GPL-2.0-only"

  # URL and SHA256 hash for ARM Mac
  on_macos do
    if Hardware::CPU.arm?
      url "https://github.com/Mustafif/MufiZ/releases/download/v0.9.0/mufiz_0.9.0_aarch64-macos.zip"
      sha256 "22db7700c70a5cbcf464439878190512ce48ad57b2a3603b78b7c1b69d3fd203"
    else
      # URL and SHA256 hash for Intel Mac
      url "https://github.com/Mustafif/MufiZ/releases/download/v0.9.0/mufiz_0.9.0_x86_64-macos.zip"
      sha256 "92f9efbeac2f746a393c95ec838d0d0e7cbc3a99782c8ce26ae46bbeb0475a78"
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
