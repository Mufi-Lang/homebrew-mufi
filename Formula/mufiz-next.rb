class MufizNext < Formula
  desc "Mufi Lang with Ziggyness (experimental)"
  homepage "https://github.com/Mustafif/MufiZ"

  tag = "next-experimental"
  version = "0.8.0"

  url "https://github.com/Mustafif/MufiZ/releases/download/#{tag}/mufiz_#{version}_x86_64-linux.zip"
  sha256 "1432154114a64365842620e407e2b5b9f266a6cb744ff0e46ee5cd353d152887"
  license "GPL-2.0-only"

  # URL and SHA256 hash for ARM Mac
  on_macos do
    if Hardware::CPU.arm?
      url "https://github.com/Mustafif/MufiZ/releases/download/#{tag}/mufiz_#{version}_aarch64-macos.zip"
      sha256 "0738eebf940425e0dcb005a3932f2ae58c9a8487673fdd55a59dca95d08130e4"
    else
      # URL and SHA256 hash for Intel Mac
      url "https://github.com/Mustafif/MufiZ/releases/download/#{tag}/mufiz_#{version}_x86_64-macos.zip"
      sha256 "0067cfba2c410a2436f440d7f6efa4de3fda2ad1de918970850c1ec9e4cbc030"
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
