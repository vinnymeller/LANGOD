{
  description = "randomly thrown together dev environment for learning a bunch of languages";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/master";
    flake-utils.url = "github:numtide/flake-utils";
    rust-overlay.url = "github:oxalica/rust-overlay";

  };

  outputs = { self, flake-utils, nixpkgs, rust-overlay, ... }@inputs:

    flake-utils.lib.eachDefaultSystem (system:

      let
        rustOverlay = import rust-overlay;
        overlays = [ rustOverlay ];
        pkgs = import nixpkgs {
            inherit system overlays;
        };
        ocamlPackages = pkgs.ocaml-ng.ocamlPackages;
        rustVersion = pkgs.rust-bin.selectLatestNightlyWith (toolchain: toolchain.default);
      in
      {
        formatter = pkgs.nixpkgs-fmt;

        devShells.default = pkgs.mkShell {

          buildInputs = with pkgs; [
            # ocaml shit
            dune_3
            opam
            ocamlPackages.findlib
            ocamlPackages.graphics
            ocamlPackages.ocaml
            ocamlPackages.utop
            ocamlPackages.opium

            # haskell shit
            ghc

            # rust shit
            rustVersion
            rust-analyzer

            # python
            python312

          ];
        };
      }

    );
}
