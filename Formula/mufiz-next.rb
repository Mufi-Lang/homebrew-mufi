class MufizNext < Formula
  desc "Mufi Lang with Ziggyness (experimental)"
  homepage "https://github.com/Mustafif/MufiZ"

  tag = "next-experimental"
  version = "0.8.0"

  url "https://github.com/Mustafif/MufiZ/releases/download/#{tag}/mufiz_#{version}_x86_64-linux.zip"
  sha256 "88583d69339e2ac58db3ada2d84b71befd1fea1d87fe4c8cf8e4dae07349d37e"
  license "GPL-2.0-only"

  # URL and SHA256 hash for ARM Mac
  on_macos do
    if Hardware::CPU.arm?
      url "https://github.com/Mustafif/MufiZ/releases/download/#{tag}/mufiz_#{version}_aarch64-macos.zip"
      sha256 "a710de1ce2094df6935785b4f64e9016bb7ed65719468c8c1bf5051ce4038008"
    else
      # URL and SHA256 hash for Intel Mac
      url "https://github.com/Mustafif/MufiZ/releases/download/#{tag}/mufiz_#{version}_x86_64-macos.zip"
      sha256 "3052ad7f0e51388fde37c7a1b97b6b4bbec4f8cc5b55cdf934a48f356ebd9574"
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
