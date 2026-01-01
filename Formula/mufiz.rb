class Mufiz < Formula
  desc "Mufi Lang with Ziggyness"
  homepage "https://github.com/Mustafif/MufiZ"

  version = "0.10.0"

  url "https://github.com/Mustafif/MufiZ/releases/download/v0.10.0/mufiz_0.10.0_x86_64-linux.zip"
  sha256 "4cd5d0b505e6bbc5e9f9162843fcc83e594c059fbea8e2df1a8cb3822214168e"
  license "GPL-2.0-only"

  # URL and SHA256 hash for ARM Mac
  on_macos do
    if Hardware::CPU.arm?
      url "https://github.com/Mustafif/MufiZ/releases/download/v0.10.0/mufiz_0.10.0_aarch64-macos.zip"
      sha256 "b2769da0f52eb27cf0a5e67ab19b10f7a75006ec553b8304c4b95137b825d2cd"
    else
      # URL and SHA256 hash for Intel Mac
      url "https://github.com/Mustafif/MufiZ/releases/download/v0.10.0/mufiz_0.10.0_x86_64-macos.zip"
      sha256 "d9c4f33c5f2a5bee832e893965fcadd81ecbe08ee66d9178bae8a2b6c2a2db88"
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
