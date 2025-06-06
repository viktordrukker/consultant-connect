/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  images: {
    domains: ['consultant-photos.s3.amazonaws.com'],
  },
  experimental: {
    serverActions: true,
  },
};

module.exports = nextConfig;
