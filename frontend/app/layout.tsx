import './globals.css';

export const metadata = {
  title: 'Consultant Connect',
  description: 'Connect with expert consultants instantly',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
