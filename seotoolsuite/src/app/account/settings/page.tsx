import { Metadata } from "next";
import SettingsComponent from "./SettingsComponent";

export const metadata: Metadata = {
  title: "Settings | SEOToolSuite",
  robots: {
    index: false,
  },
};

export default function SettingsPage() {
  return <SettingsComponent />;
}
