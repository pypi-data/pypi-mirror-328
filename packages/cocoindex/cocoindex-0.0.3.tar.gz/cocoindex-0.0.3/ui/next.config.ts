import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'standalone',

  // See https://huggingface.co/docs/transformers.js/tutorials/next#step-2-install-and-configure-transformersjs
  webpack: (config) => {
    // See https://webpack.js.org/configuration/resolve/#resolvealias
    config.resolve.alias = {
      ...config.resolve.alias,
      "sharp$": false,
      "onnxruntime-node$": false,
    }
    return config;
  },

  serverExternalPackages: ['sharp', 'onnxruntime-node'],
};

export default nextConfig;
