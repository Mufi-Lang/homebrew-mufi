class MufizNext < Formula
  desc "Mufi Lang with Ziggyness (experimental)"
  homepage "https://github.com/Mustafif/MufiZ"

  tag = "next-experimental"
  version = "0.10.0"

  url "https://github.com/Mustafif/MufiZ/releases/download/next-experimental/mufiz_0.10.0_x86_64-linux.zip"
  sha256 "3e1c1e2c88b644aaf39c9846cff9e74d4cd9c4e6a9122ebf7e3478e8d7b1482c"
  license "GPL-2.0-only"

  # URL and SHA256 hash for ARM Mac
  on_macos do
    if Hardware::CPU.arm?
      url "https://github.com/Mustafif/MufiZ/releases/download/next-experimental/mufiz_0.10.0_aarch64-macos.zip"
      sha256 "7c0f813c23e0c5b443f921d6f9ab312f89701a87f639e1b85f6a971cd3541561"
    else
      # URL and SHA256 hash for Intel Mac
      url "https://github.com/Mustafif/MufiZ/releases/download/next-experimental/mufiz_0.10.0_x86_64-macos.zip"
      sha256 "d509dbba6db312f113948334904bbffad1ce53a4dca91c63c7eeba7450f30128"
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
