(ns day_01.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "01")

(defn get-lines
  "Read in inputs as seq of integers."
  [file]
  (->> file
       slurp
       str/split-lines
       (map read-string)))

(defn two-sum
  [inputs target]
  (loop [l  inputs
         seen #{}]
    (when-let [curr (first l)]
      (if-let [match (seen (- target curr))]
        (* curr match)
        (recur (rest l) (conj seen curr))))))

(defn three-sum
  [inputs target]
  (letfn [(search [x]
            (when-let [yz (two-sum inputs (- target x))]
              (* x yz)))]
    (some search inputs)))

(defn part1
  [_]
  (let [inputs (get-lines "day_01/inputs.txt")
        target 2020]
    (two-sum inputs target)))

(defn part2
  [_]
  (let [inputs (get-lines "day_01/inputs.txt")
        target 2020]
    (three-sum inputs target)))

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)

(comment
  (let [inputs [1721 979 366 299 675 1456]
        target 2020]
    (two-sum inputs target))

  (let [inputs [1721 979 366 299 675 1456]
        target 2020]
    (three-sum inputs target)))
