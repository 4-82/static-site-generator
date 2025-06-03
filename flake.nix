{
  inputs = {nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";};
  outputs = {
    self,
    nixpkgs,
  }: let
    systems = ["aarch64-linux" "aarch64-darwin" "x86_64-linux"];
    all = nixpkgs.lib.genAttrs systems;
  in {
    devShells = all (system: let
      pkgs = nixpkgs.legacyPackages.${system}; in {
      default = pkgs.mkShell {
        packages = builtins.attrValues {
          inherit (pkgs) nil go gh;
          inherit (pkgs.python312Packages) python-lsp-server ruff;
          bootdev = pkgs.callPackage ./bootdev.nix {};
        };
      };
    });
  };
}
