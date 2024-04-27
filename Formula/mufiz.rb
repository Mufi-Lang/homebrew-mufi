class Mufiz < Formula
  desc "Mufi Lang with Ziggyness"
  homepage "https://github.com/Mustafif/MufiZ"

  url "https://github.com/Mustafif/MufiZ/releases/download/v0.6.0/mufiz_0.6.0_x86_64-linux.zip"
  sha256 "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  license "GPL-2.0-only"

  # URL and SHA256 hash for ARM Mac
  on_macos do
    if Hardware::CPU.arm?
      url "https://github.com/Mustafif/MufiZ/releases/download/v0.6.0/mufiz_0.6.0_aarch64-macos.zip"
      sha256 "111ade40dbd08a8a0f763bf3243c0582c46a55b91524521f642bdc0af8076889"
    else
      # URL and SHA256 hash for Intel Mac
      url "https://github.com/Mustafif/MufiZ/releases/download/v0.6.0/mufiz_0.6.0_x86_64-macos.zip"
      sha256 "0eb96113539f19bfba078ea171c91fd1beede8e241ba103eee2a121d41ad3b53"
    end
  end

  def install
    # Extract the contents of the zip archive
    system "unzip", "-q", cached_download.to_s, "-d", "#{buildpath}/mufiz"
    bin.install "#{buildpath}/mufiz/mufiz" # Adjust the binary name if necessary
  end

  test do
    # Add a simple test here if possible
    system "#{bin}/mufiz", "--version"
  end
end
