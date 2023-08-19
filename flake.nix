{
  description = "OCaml dev environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";

  };

  outputs = { self, flake-utils, nixpkgs, ... }@inputs:

    flake-utils.lib.eachDefaultSystem (system:

      let
        pkgs = nixpkgs.legacyPackages.${system};
        ocamlPackages = pkgs.ocaml-ng.ocamlPackages;
      in
      {
        formatter = pkgs.nixpkgs-fmt;

        devShells.default = pkgs.mkShell {

          buildInputs = with pkgs; [
            dune_3
            opam
            ocamlPackages.findlib
            ocamlPackages.graphics
            ocamlPackages.ocaml
            ocamlPackages.utop

            ocamlPackages.opium
          ];
        };
      }

    );
}
